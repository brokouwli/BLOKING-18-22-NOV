import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Constants
PARKING_RATE = 2000  # Fee per hour in Rp

# Global Data Storage
parking_data = []
sorted_by_exit = []
sorted_by_payment = []

# Utility Functions
def calculate_fee(entry_time, exit_time):
    """Calculate parking fee based on entry and exit times."""
    try:
        fmt = "%H:%M"  # Expected time format
        entry = datetime.strptime(entry_time, fmt)
        exit = datetime.strptime(exit_time, fmt)
        duration = (exit - entry).total_seconds() / 3600  # Convert to hours
        fee = max(1, int(duration)) * PARKING_RATE  # Minimum 1 hour fee
        return fee
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Use HH:MM")
        return None

def add_vehicle():
    """Add vehicle data to the system."""
    plate = nopol_entry.get()
    entry = entry_time_entry.get()
    exit = exit_time_entry.get()

    if not plate or not entry or not exit:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    fee = calculate_fee(entry, exit)
    if fee is None:
        return  # Exit if there's an error in time format

    # Add to data and sort
    parking_data.append({"plate": plate, "entry": entry, "exit": exit, "fee": fee})
    update_tables()

    # Clear input fields
    nopol_entry.delete(0, tk.END)
    entry_time_entry.delete(0, tk.END)
    exit_time_entry.delete(0, tk.END)
    biaya_label.config(text="Rp 0")

def update_tables():
    """Update display tables with sorted data."""
    global sorted_by_exit, sorted_by_payment

    # Sort data
    sorted_by_exit = sorted(parking_data, key=lambda x: x["exit"], reverse=True)
    sorted_by_payment = sorted(parking_data, key=lambda x: x["fee"], reverse=True)

    # Update tables
    for row in exit_table.get_children():
        exit_table.delete(row)
    for row in payment_table.get_children():
        payment_table.delete(row)

    for data in sorted_by_exit:
        exit_table.insert("", tk.END, values=(data["plate"], data["entry"], data["exit"], f"Rp {data['fee']}"))
    for data in sorted_by_payment:
        payment_table.insert("", tk.END, values=(data["plate"], data["fee"]))

def search_vehicle():
    """Search vehicle by plate number."""
    search_plate = search_entry.get()
    for data in parking_data:
        if data["plate"] == search_plate:
            messagebox.showinfo("Search Result", f"Plate: {data['plate']}\nEntry: {data['entry']}\nExit: {data['exit']}\nFee: Rp {data['fee']}")
            return
    messagebox.showwarning("Not Found", "Vehicle not found!")

# GUI Setup
window = tk.Tk()
window.title("Parking Management System")
window.geometry("700x600")

# Input Form
input_frame = ttk.LabelFrame(window, text="Input Form")
input_frame.pack(padx=10, pady=10, fill="x")

ttk.Label(input_frame, text="Cari NoPol:").grid(row=0, column=0, padx=5, pady=5)
search_entry = ttk.Entry(input_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = ttk.Button(input_frame, text="Search", command=search_vehicle)
search_button.grid(row=0, column=2, padx=5, pady=5)

ttk.Label(input_frame, text="No Plat Polisi:").grid(row=1, column=0, padx=5, pady=5)
nopol_entry = ttk.Entry(input_frame)
nopol_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Waktu Masuk (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
entry_time_entry = ttk.Entry(input_frame)
entry_time_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Waktu Keluar (HH:MM):").grid(row=3, column=0, padx=5, pady=5)
exit_time_entry = ttk.Entry(input_frame)
exit_time_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Biaya:").grid(row=4, column=0, padx=5, pady=5)
biaya_label = ttk.Label(input_frame, text="Rp 0")
biaya_label.grid(row=4, column=1, padx=5, pady=5)

submit_button = ttk.Button(input_frame, text="Submit", command=add_vehicle)
submit_button.grid(row=5, column=0, columnspan=3, pady=10)

# Display Tables
exit_table_frame = ttk.LabelFrame(window, text="List Pelanggan Urut Terakhir Keluar")
exit_table_frame.pack(padx=10, pady=10, fill="x")

exit_table = ttk.Treeview(exit_table_frame, columns=("Plate", "Entry", "Exit", "Fee"), show="headings")
exit_table.pack(fill="x")
exit_table.heading("Plate", text="No. Polisi")
exit_table.heading("Entry", text="Waktu Masuk")
exit_table.heading("Exit", text="Waktu Keluar")
exit_table.heading("Fee", text="Biaya")

payment_table_frame = ttk.LabelFrame(window, text="List Pelanggan Banyak Bayar")
payment_table_frame.pack(padx=10, pady=10, fill="x")

payment_table = ttk.Treeview(payment_table_frame, columns=("Plate", "Fee"), show="headings")
payment_table.pack(fill="x")
payment_table.heading("Plate", text="No. Polisi")
payment_table.heading("Fee", text="Biaya")

# Run App
window.mainloop()