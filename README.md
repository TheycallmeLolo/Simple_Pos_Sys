# Simple Cashier & Manager POS System

A Python terminal application that simulates a retail checkout system. It separates the daily cashier operations from the manager's reporting dashboard using an SQLite database.

## 🚀 Features

* **Cashier System:** Adds items to a temporary cart and calculates totals quickly in memory.
* **Manager Dashboard:** Saves completed sales permanently in a database and displays total profits and discounts.
* **Smart Discount:** Automatically asks the cashier if they want to apply a 10% discount if the bill is over $500.
* **Database Seeding:** Includes a script to fill the database with random sales for instant testing.
* **Error Handling:** Uses `try-except` blocks to stop the app from crashing if someone type letters instead of prices.

---

## 💾 How to Run the Project

1. **Clone the repository to your computer:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Generate mock data for testing (Recommended):**
   Run this script first to fill the manager's database with 20 random past sales.
   ```bash
   python seed_db.py
   ```

3. **Start the main application:**
   ```bash
   python main.py
   ```

---

## 🛠️ Tech Stack & Topics Learned

* **Language:** Python 3
* **Database:** SQLite3 (Built-in relational database)
* **Core Concepts:** Loops, Dictionaries, Functions, File/Database connection, and Input Validation.

---

## 📋 File Structures

* `main.py`: The main program containing the cashier cart and manager menus.
* `seed_db.py`: A helper script that creates random database rows for testing.
