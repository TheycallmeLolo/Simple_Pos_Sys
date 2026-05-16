import sqlite3
from datetime import datetime


current_order = []

def db_connect():
    conn = sqlite3.connect('sales_report.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS daily_sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    subtotal REAL,
                    discount_issued REAL,
                    final_total REAL
                 )''')
    conn.commit()
    return conn, c


def cashier_add_item():
    item_name = input("Enter item name: ").strip()
    if not item_name: return
    try:
        price = float(input("Enter price: "))
        amount = int(input("Enter amount: "))
        if price <= 0 or amount <= 0:
            print("❌ Invalid price or amount.")
            return
    except ValueError:
        print("❌ Invalid numbers.")
        return

    current_order.append({"name": item_name, "price": price, "amount": amount})
    print(f"✔️ Added {item_name} to current cart.")

def cashier_print_cart():
    if not current_order:
        print("🛒 Cart is empty.")
        return
    print("\n--- Current Customer Cart ---")
    for item in current_order:
        print(f"🔹 {item['name']} - ${item['price']} x {item['amount']} = ${item['price'] * item['amount']:.2f}")

def cashier_checkout(c, conn):
    if not current_order:
        print("❌ Cannot checkout an empty cart.")
        return
    
       
    subtotal = sum(item['price'] * item['amount'] for item in current_order)
    disc = 0.0
    
    
    if subtotal > 500:
        print(f"\n📢 Order total is ${subtotal:.2f} (Eligible for 10% discount!)")
        ask_discount = input("Do you want to apply the 10% discount? (y/n): ").strip().lower()
        if ask_discount == 'y':
            disc = subtotal * 0.1
            print("✅ Discount applied successfully.")
        else:
            print("🚫 Discount skipped by cashier.")
    
    final_total = subtotal - disc
    
    
    print("\n========================")
    print("      RECEIPT           ")
    print("========================")
    for item in current_order:
        print(f"🔹 {item['name']} - ${item['price']} x {item['amount']} = ${item['price'] * item['amount']:.2f}")
    print("------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    if disc > 0:
        print(f"Discount (10%): -${disc:.2f}")
    print(f"FINAL PAID: ${final_total:.2f}")
    print("========================")

    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO daily_sales (timestamp, subtotal, discount_issued, final_total) VALUES (?, ?, ?, ?)",
              (timestamp, subtotal, disc, final_total))
    conn.commit()
    
    
    current_order.clear()
    print("✅ Payment Confirmed & Saved to Manager Dashboard.")



def manager_view_reports(c):
    print("\n=== 📊 MANAGER DASHBOARD ===")
    c.execute("SELECT COUNT(*), SUM(subtotal), SUM(discount_issued), SUM(final_total) FROM daily_sales")
    stats = c.fetchone()
    
    if not stats or stats[0] == 0:
        print("No sales recorded yet today.")
        return
        
    total_orders, total_sub, total_disc, net_profit = stats
    print(f"📈 Total Orders Processed: {total_orders}")
    print(f"💰 Gross Sales (Before Discounts): ${total_sub:.2f}")
    print(f"📉 Total Discounts Given: ${total_disc:.2f}")
    print(f"💵 Net Profit (Actual Cash In): ${net_profit:.2f}")
    print("-----------------------------------")
    
    
    print("📋 Last 5 Invoices Details:")
    c.execute("SELECT id, timestamp, final_total FROM daily_sales ORDER BY id DESC LIMIT 5")
    for row in c.fetchall():
        print(f"  Invoice #{row[0]} | {row[1]} | Total: ${row[2]:.2f}")

def main():
    conn, c = db_connect()
    while True:
        print("\n🌐 MAIN SYSTEM")
        print("1. [Cashier] Add item to cart")
        print("2. [Cashier] View current cart")
        print("3. [Cashier] Confirm Payment & Checkout")
        print("4. [Manager] View Dashboard & Profits")
        print("5. Exit System")
        choice = input("Select role/action: ").strip()
        
        if choice == '1': cashier_add_item()
        elif choice == '2': cashier_print_cart()
        elif choice == '3': cashier_checkout(c, conn)
        elif choice == '4': manager_view_reports(c)
        elif choice == '5': break
        else: print("Invalid choice.")
        
    conn.close()

if __name__ == "__main__":
    main()
