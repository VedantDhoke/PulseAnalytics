import tkinter as tk
from tkinter import StringVar, OptionMenu
import pymysql

def fetch_dates_from_database():
    conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT DateColumn FROM cbc")  # Fetch unique dates from the table
    dates = [date[0] for date in cursor.fetchall()]  # Extract dates from the fetched data
    conn.close()
    return dates

def fetch_row_from_database(date_value):
    conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cbc WHERE DateColumn = %s", (date_value,))
    row = cursor.fetchone()  # Fetch the first row that matches the date
    conn.close()
    return row

def on_date_selected():
    selected_date = date_var.get()
    row = fetch_row_from_database(selected_date)
    if row:
        for i, value in enumerate(row[1:]):  # Skip the date value (first column)
            text_fields[i].delete(0, tk.END)
            text_fields[i].insert(tk.END, str(value))
    else:
        # Clear text fields if no matching row found
        for text_field in text_fields:
            text_field.delete(0, tk.END)

# Create a Tkinter window
root = tk.Tk()
root.title("Fetch Row Data by Date")

# Create a Label and Dropdown for Date selection
date_label = tk.Label(root, text="Select Date:")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_var = StringVar()
dates = fetch_dates_from_database()
date_dropdown = OptionMenu(root, date_var, *dates)
date_dropdown.grid(row=0, column=1, padx=5, pady=5)
date_var.trace('w', lambda *args: on_date_selected())  # Call on_date_selected when date_var changes

# Create Text Fields for displaying row data
text_fields = []
for i in range(6):
    label = tk.Label(root, text=f"Value {i+1}:")
    label.grid(row=i+1, column=0, padx=5, pady=5)
    text_field = tk.Entry(root)
    text_field.grid(row=i+1, column=1, padx=5, pady=5)
    text_fields.append(text_field)

# Start the Tkinter event loop
root.mainloop()
