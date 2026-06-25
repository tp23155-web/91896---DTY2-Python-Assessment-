import tkinter as tk
from tkinter import ttk, messagebox
import random
def submit_details():
    name = name_entry.get().strip().lower()
    item = item_entry.get().strip().lower()
    quantity = quantity_entry.get().strip()
    item_status = status_box.get() 

    # 1. Check for Boxes
    if name == "":
        messagebox.showerror("Input Error", "Name cannot be blank")
        return
    if item == "":
        messagebox.showerror("Input Error", "Item cannot be blank")
        return
    if quantity == "":
        messagebox.showerror("Input Error", "Quantity cannot be blank")
        return

    # 2. Validate and convert quantity
    try:
        new_quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "For quantity please enter a whole number (integer) without decimals.")
        return

    # 3. Check number boundary cases
    if new_quantity <= 0:
        messagebox.showerror("Error", "Quantity must be greater than 0")
        return
    elif new_quantity > 500:
        messagebox.showerror("Error", "Quantity must be 500 or less")
        return

    # Receipt
    # Generate a unique random number between 1 and 99999 that wont repeat
    receipts = random.sample(range(1, 100000),1)
    

    # If everything passes, print for testing
    print(name)
    print(item)
    print(new_quantity)
    print(item_status)
    print(receipts)
    

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Party Hire Shop")
root.geometry ("300x300")

title_label = ttk.Label(root, text="Party Hire Shop", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=1, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = ttk. Entry(root, width= 25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Item: "). grid(row=2, column=0, sticky="e")
item_entry= ttk.Entry(root, width=25)
item_entry.grid(row=2, column =1)

ttk.Label(root, text="Quantity"). grid(row=3, column=0, sticky="e")
quantity_entry= ttk.Entry(root, width=25)
quantity_entry.grid(row=3, column =1)


ttk.Label(root, text= "Hired/Returned"). grid(row=4, column=0, sticky="e")
status_box = ttk.Combobox(root, values = ["Hired", "Returned"], state = "readonly")
status_box.grid(row=4, column=1)
status_box.current(0)

submit_btn = ttk.Button(root, text= "Enter Details", command = submit_details)
submit_btn.grid(row=5, column=1, pady=10)

finish_btn = ttk.Button(root, text="Quit", command = exit_program)
finish_btn.grid(row=7, column=1, pady=10)


root.mainloop() 
