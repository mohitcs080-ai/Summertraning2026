import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

def add_expense():
    d = entry_date.get()
    c = combo.get()
    a = entry_amount.get()
    desc = entry_desc.get()

    if d == "" or c == "" or a == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO expenses(date,category,amount,description) VALUES(?,?,?,?)",
        (d, c, float(a), desc)
    )
    conn.commit()

    show_data()

    entry_amount.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def show_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT  FROM expenses")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

def delete_expense():
    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected)["values"]

    cursor.execute("DELETE FROM expenses WHERE id=?", (values[0],))
    conn.commit()

    show_data()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("850x500")

tk.Label(root, text="Date").grid(row=0, column=0)

entry_date = tk.Entry(root)
entry_date.insert(0, str(date.today()))
entry_date.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)

combo = ttk.Combobox(root)
combo['values'] = (
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Health",
    "Education",
    "Other"
)
combo.grid(row=1, column=1)

tk.Label(root, text="Amount").grid(row=2, column=0)

entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Label(root, text="Description").grid(row=3, column=0)

entry_desc = tk.Entry(root)
entry_desc.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0)

tk.Button(root, text="Delete", command=delete_expense).grid(row=4, column=1)

columns = ("ID", "Date", "Category", "Amount", "Description")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.grid(row=5, column=0, columnspan=4)

show_data()

root.mainloop()

conn.close()