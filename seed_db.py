import sqlite3
import random
from datetime import datetime, timedelta

def seed_database(num_invoices=20):
    # 1. Connect to the sales database
    conn = sqlite3.connect('sales_report.db')
    c = conn.cursor()
    
    # 2. Ensure the manager's table exists
    c.execute('''CREATE TABLE IF NOT EXISTS daily_sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    subtotal REAL,
                    discount_issued REAL,
                    final_total REAL
                 )''')
    
    # Clear old data to prevent duplication during testing
    c.execute("DELETE FROM daily_sales")
    
    print(f"⏳ Generating {num_invoices} mock invoices for the Manager Dashboard...")
    
    fake_invoices = []
    
    # 3. Generate random historical invoices
    for i in range(num_invoices):
        # Generate random subtotal between $20.0 and $1200.0
        subtotal = round(random.uniform(20.0, 1200.0), 2)
        
        # Apply the 10% discount rule logically if subtotal > 500
        discount_issued = 0.0
        if subtotal > 500:
            # Simulate that cashiers accepted the discount 85% of the time
            if random.random() < 0.85:
                discount_issued = round(subtotal * 0.1, 2)
                
        final_total = round(subtotal - discount_issued, 2)
        
        # Generate random times over the last few days to make reports look realistic
        random_minutes_ago = random.randint(1, 4320)  # up to 3 days ago
        invoice_time = (datetime.now() - timedelta(minutes=random_minutes_ago)).strftime("%Y-%m-%d %H:%M:%S")
        
        fake_invoices.append((invoice_time, subtotal, discount_issued, final_total))
    
    # 4. Bulk insert for high performance
    c.executemany("INSERT INTO daily_sales (timestamp, subtotal, discount_issued, final_total) VALUES (?, ?, ?, ?)", 
                  fake_invoices)
    
    conn.commit()
    conn.close()
    print("✅ Database successfully populated with realistic manager analytics data!")

if __name__ == "__main__":
    seed_database(20)
