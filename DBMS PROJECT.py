import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

# -----------------------------
# Database Setup
# -----------------------------
def init_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# -----------------------------
# Add Expense
# -----------------------------
def add_expense():
    category = category_var.get()
    amount = amount_var.get()
    if category and amount:
        try:
            amount = float(amount)
            conn = sqlite3.connect("finance.db")
            cursor = conn.cursor()
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
                           (category, amount, date))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Added {category} - ₹{amount}")
            amount_var.set("")
            load_expenses()
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
    else:
        messagebox.showerror("Error", "Please enter category and amount")

# -----------------------------
# Load Expenses
# -----------------------------
def load_expenses():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        tree.insert("", tk.END, values=row)

# -----------------------------
# Monthly Report (Chart)
# -----------------------------
def monthly_report():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses 
        WHERE strftime('%m', date) = strftime('%m', 'now')
        GROUP BY category
    """)
    rows = cursor.fetchall()
    conn.close()

    if rows:
        categories = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%")
        plt.title("Monthly Expense Breakdown")
        plt.show()
    else:
        messagebox.showinfo("Report", "No expenses recorded this month")

# -----------------------------
# GUI Setup
# -----------------------------
init_db()
root = tk.Tk()
root.title("Personal Finance Tracker")

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Category:").grid(row=0, column=0)
category_var = tk.StringVar()
tk.Entry(frame, textvariable=category_var).grid(row=0, column=1)

tk.Label(frame, text="Amount:").grid(row=1, column=0)
amount_var = tk.StringVar()
tk.Entry(frame, textvariable=amount_var).grid(row=1, column=1)

tk.Button(frame, text="Add Expense", command=add_expense).grid(row=2, columnspan=2, pady=5)

# Expense Table
tree = ttk.Treeview(root, columns=("ID", "Category", "Amount", "Date"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Date", text="Date")
tree.pack(pady=10)

tk.Button(root, text="Monthly Report (Chart)", command=monthly_report).pack(pady=5)

load_expenses()
root.mainloop()
