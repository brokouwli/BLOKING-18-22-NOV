import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_total():
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        total = price * quantity
        total_label.config(text=f"Total: Rp.{total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid price and quantity.")

# Create the main window
root = tk.Tk()
root.title("Cashier Program")

# Create labels and entry fields
price_label = tk.Label(root, text="Harga:")
price_label.grid(row=0, column=0, padx=10, pady=10)
price_entry = tk.Entry(root)
price_entry.grid(row=0, column=1, padx=10, pady=10)

quantity_label = tk.Label(root, text="Kuantitas:")
quantity_label.grid(row=1, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Hitung Total", command=calculate_total)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create total label
total_label = tk.Label(root, text="Total: Rp.0.00")
total_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()