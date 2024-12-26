import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the SQLite database with the new path
db_path = r"C:\Users\abano\Desktop\DB Project\DataBase\Final-HotelReservation.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Function to insert data into the 'guests' table
def insert_guest():
    passport_number = entry_guest_passport.get()
    name = entry_guest_name.get()
    phone_number = entry_guest_phone.get()
    
    if passport_number and name and phone_number:
        c.execute("INSERT INTO guests (passport, name, phone_number) VALUES (?, ?, ?)", 
                  (passport_number, name, phone_number))
        conn.commit()
        messagebox.showinfo("Success", "Guest added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function to insert data into the 'rooms' table
def insert_room():
    room_number = entry_room_number.get()
    room_view = entry_room_view.get()
    price = entry_room_price.get()
    
    if room_number and room_view and price:
        c.execute("INSERT INTO rooms (room_number, room_view, price) VALUES (?, ?, ?)", 
                  (room_number, room_view, float(price)))
        conn.commit()
        messagebox.showinfo("Success", "Room added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function to insert data into the 'bookings' table
def insert_booking():
    guest_passport = entry_booking_guest_passport.get()
    room_number = entry_booking_room_number.get()
    check_in_date = entry_booking_check_in.get()
    check_out_date = entry_booking_check_out.get()
    total_amount = entry_booking_total_amount.get()
    
    if guest_passport and room_number and check_in_date and check_out_date and total_amount:
        c.execute("INSERT INTO bookings (guest_passport, room_number, check_in_date, check_out_date, total_amount) VALUES (?, ?, ?, ?, ?)", 
                  (guest_passport, room_number, check_in_date, check_out_date, float(total_amount)))
        conn.commit()
        messagebox.showinfo("Success", "Booking added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function to insert data into the 'services' table
def insert_service():
    service_name = entry_service_name.get()
    price = entry_service_price.get()
    
    if service_name and price:
        c.execute("INSERT INTO services (service_name, price) VALUES (?, ?)", 
                  (service_name, float(price)))
        conn.commit()
        messagebox.showinfo("Success", "Service added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function to insert data into the 'billing' table
def insert_billing():
    booking_id = entry_billing_booking_id.get()
    service_id = entry_billing_service_id.get()
    amount = entry_billing_amount.get()
    
    if booking_id and service_id and amount:
        c.execute("INSERT INTO billing (booking_id, service_id, amount) VALUES (?, ?, ?)", 
                  (booking_id, service_id, float(amount)))
        conn.commit()
        messagebox.showinfo("Success", "Billing added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function to clear the input fields
def clear_entries():
    entry_guest_passport.delete(0, tk.END)
    entry_guest_name.delete(0, tk.END)
    entry_guest_phone.delete(0, tk.END)
    entry_room_number.delete(0, tk.END)
    entry_room_view.delete(0, tk.END)
    entry_room_price.delete(0, tk.END)
    entry_booking_guest_passport.delete(0, tk.END)
    entry_booking_room_number.delete(0, tk.END)
    entry_booking_check_in.delete(0, tk.END)
    entry_booking_check_out.delete(0, tk.END)
    entry_booking_total_amount.delete(0, tk.END)
    entry_service_name.delete(0, tk.END)
    entry_service_price.delete(0, tk.END)
    entry_billing_booking_id.delete(0, tk.END)
    entry_billing_service_id.delete(0, tk.END)
    entry_billing_amount.delete(0, tk.END)

# Function to display the data from any table
def display_data(table_name):
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    if rows:
        display_window = tk.Toplevel(root)
        display_window.title(f"{table_name} List")
        for index, row in enumerate(rows):
            tk.Label(display_window, text=str(row)).grid(row=index, column=0)
    else:
        messagebox.showinfo("No Data", f"No data found in {table_name}.")

# Function to delete a record from any table
def delete_record(table_name, record_id):
    try:
        c.execute(f"DELETE FROM {table_name} WHERE {table_name[:-1]}_id = ?", (record_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Record deleted from {table_name}!")
        clear_entries()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to delete record: {e}")

# Function to update a record in any table
def update_record(table_name, record_id, column_name, new_value):
    try:
        c.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE {table_name[:-1]}_id = ?", 
                  (new_value, record_id))
        conn.commit()
        messagebox.showinfo("Success", f"Record updated in {table_name}!")
        clear_entries()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to update record: {e}")

# GUI Setup
root = tk.Tk()
root.title("Hotel Reservation System")

# Guest section
tk.Label(root, text="Passport Number:").grid(row=0, column=0)
entry_guest_passport = tk.Entry(root)
entry_guest_passport.grid(row=0, column=1)

tk.Label(root, text="Guest Name:").grid(row=1, column=0)
entry_guest_name = tk.Entry(root)
entry_guest_name.grid(row=1, column=1)

tk.Label(root, text="Guest Phone Number:").grid(row=2, column=0)
entry_guest_phone = tk.Entry(root)
entry_guest_phone.grid(row=2, column=1)

tk.Button(root, text="Insert Guest", command=insert_guest).grid(row=3, column=0, pady=5)
tk.Button(root, text="Delete Guest", command=lambda: delete_record("guests", entry_guest_passport.get())).grid(row=3, column=1, pady=5)
tk.Button(root, text="Update Guest", command=lambda: update_record("guests", entry_guest_passport.get(), "name", entry_guest_name.get())).grid(row=3, column=2, pady=5)

# Room section
tk.Label(root, text="Room Number:").grid(row=4, column=0)
entry_room_number = tk.Entry(root)
entry_room_number.grid(row=4, column=1)

tk.Label(root, text="Room View:").grid(row=5, column=0)
entry_room_view = tk.Entry(root)
entry_room_view.grid(row=5, column=1)

tk.Label(root, text="Room Price:").grid(row=6, column=0)
entry_room_price = tk.Entry(root)
entry_room_price.grid(row=6, column=1)

tk.Button(root, text="Insert Room", command=insert_room).grid(row=7, column=0, pady=5)
tk.Button(root, text="Delete Room", command=lambda: delete_record("rooms", entry_room_number.get())).grid(row=7, column=1, pady=5)
tk.Button(root, text="Update Room", command=lambda: update_record("rooms", entry_room_number.get(), "price", entry_room_price.get())).grid(row=7, column=2, pady=5)

# Booking section
tk.Label(root, text="Guest Passport:").grid(row=8, column=0)
entry_booking_guest_passport = tk.Entry(root)
entry_booking_guest_passport.grid(row=8, column=1)

tk.Label(root, text="Room Number:").grid(row=9, column=0)
entry_booking_room_number = tk.Entry(root)
entry_booking_room_number.grid(row=9, column=1)

tk.Label(root, text="Check-in Date:").grid(row=10, column=0)
entry_booking_check_in = tk.Entry(root)
entry_booking_check_in.grid(row=10, column=1)

tk.Label(root, text="Check-out Date:").grid(row=11, column=0)
entry_booking_check_out = tk.Entry(root)
entry_booking_check_out.grid(row=11, column=1)

tk.Label(root, text="Total Amount:").grid(row=12, column=0)
entry_booking_total_amount = tk.Entry(root)
entry_booking_total_amount.grid(row=12, column=1)

tk.Button(root, text="Insert Booking", command=insert_booking).grid(row=13, column=0, pady=5)

# Service section
tk.Label(root, text="Service Name:").grid(row=14, column=0)
entry_service_name = tk.Entry(root)
entry_service_name.grid(row=14, column=1)

tk.Label(root, text="Service Price:").grid(row=15, column=0)
entry_service_price = tk.Entry(root)
entry_service_price.grid(row=15, column=1)

tk.Button(root, text="Insert Service", command=insert_service).grid(row=16, column=0, pady=5)

# Billing section
tk.Label(root, text="Booking ID:").grid(row=17, column=0)
entry_billing_booking_id = tk.Entry(root)
entry_billing_booking_id.grid(row=17, column=1)

tk.Label(root, text="Service ID:").grid(row=18, column=0)
entry_billing_service_id = tk.Entry(root)
entry_billing_service_id.grid(row=18, column=1)

tk.Label(root, text="Amount:").grid(row=19, column=0)
entry_billing_amount = tk.Entry(root)
entry_billing_amount.grid(row=19, column=1)

tk.Button(root, text="Insert Billing", command=insert_billing).grid(row=20, column=0, pady=5)

# Buttons to display data from different tables
tk.Button(root, text="Display Guests", command=lambda: display_data("guests")).grid(row=21, column=0, pady=5)
tk.Button(root, text="Display Rooms", command=lambda: display_data("rooms")).grid(row=21, column=1, pady=5)
tk.Button(root, text="Display Bookings", command=lambda: display_data("bookings")).grid(row=22, column=0, pady=5)
tk.Button(root, text="Display Services", command=lambda: display_data("services")).grid(row=22, column=1, pady=5)
tk.Button(root, text="Display Billing", command=lambda: display_data("billing")).grid(row=23, column=0, pady=5)

root.mainloop()

# Close the connection when the program ends
conn.close()
