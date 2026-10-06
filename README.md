# 💰 Personal Finance Tracker

A simple **Personal Finance Tracker** built with Python that allows users to record their daily expenses, store them in a SQLite database, view expense records, and generate a monthly expense breakdown chart.

---

## 📌 Features

- ➕ Add expenses with category and amount
- 💾 Store expense data using SQLite
- 📋 View all recorded expenses in a table
- 📅 Automatically record the date and time of each expense
- 📊 Generate monthly expense reports using charts
- ⚠️ Input validation
- 🖥️ User-friendly desktop GUI using Tkinter

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter**
- **SQLite3**
- **Matplotlib**
- **Datetime**

---

## 📂 Project Structure

```text
Personal-Finance-Tracker/
│
├── finance_tracker.py
├── finance.db
├── README.md
└── screenshots/
```

---

## ⚙️ How It Works

### Database Setup
- Creates a SQLite database named `finance.db`
- Stores expenses with:
  - ID
  - Category
  - Amount
  - Date

### Add Expense
Users can:
- Enter category
- Enter amount
- Save expenses to the database

### View Expenses
All expenses are displayed in a table format.

### Monthly Report
Generates a pie chart showing category-wise expense distribution.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Personal-Finance-Tracker.git
```

### Navigate to Project

```bash
cd Personal-Finance-Tracker
```

### Install Required Libraries

```bash
pip install matplotlib
```

> Tkinter and SQLite are included with Python by default.

---

## ▶️ Run the Project

```bash
python finance_tracker.py
```

---

## 📊 Example

| Category | Amount |
|-----------|----------|
| Food | ₹250 |
| Travel | ₹150 |
| Shopping | ₹500 |

---

## 🖥️ Screenshots

### Main Window
(Add screenshot here)

### Expense Table
(Add screenshot here)

### Monthly Chart
(Add screenshot here)

---

## 🔮 Future Enhancements

- Income Tracking
- Budget Planning
- Expense Search
- Edit/Delete Expenses
- Export to Excel/CSV
- User Authentication
- Modern UI

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python GUI Development
- SQLite Database Operations
- Data Visualization
- Event-Driven Programming
- CRUD Operations

---

## 👩‍💻 Author

**Pratheesh S Y**

B.E. Computer Science and Engineering

---

⭐ If you found this project useful, please give it a star!
