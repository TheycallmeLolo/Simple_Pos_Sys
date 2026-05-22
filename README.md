# Simple Cashier & Manager POS System

A Python terminal application that simulates a retail checkout system. It separates the daily cashier operations from the manager's reporting dashboard using an SQLite database.

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
