import tkinter as tk
from tkinter import ttk, messagebox
import random

final_name = []
item_hired = []
quantity_hired = []
item_receipts = []

def save_data():
    with open("party_hire.txt", "w") as file:

        file.write("----------------------------------------------------------------------------------------------------\n")
        file.write("Party Hire".center(100)+ "\n")
        file.write("----------------------------------------------------------------------------------------------------\n\n")

        for i in range(len(final_name)):
            file.write(f"Name: {final_name[i]}\n")
            file.write(f"Item: {item_hired[i]}\n")
            file.write(f"Qauntity: {quantity_hired[i]}\n")
            file.write(f"Receipt Number: {item_receipts[i]}\n\n")

def submit_details():
    name = name_entry.get().strip().lower()
    item = item_entry.get().strip().lower()
    quantity = quantity_entry.get().strip()

    # 1. Check for Input in Boxes
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
    print(receipts)
    save_data()

    final_name.append(name)
    item_hired.append(item)
    quantity_hired.append(new_quantity)
    item_receipts.append(receipts)


def exit_program():
    root.quit()

root = tk.Tk()
root.title("Party Hire Shop")
root.geometry ("300x400")

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

returns_label = ttk.Label(root, text="Returns", font=("Verdana", 18, "bold"))
returns_label.grid(row=5, column=1, columnspan=2, pady=10)

status_box = ttk.Combobox(root, values = [], state = "readonly")
status_box.grid(row=6, column=1)
status_box.current(0)

submit_btn = ttk.Button(root, text= "Enter Details", command = submit_details)
submit_btn.grid(row=4, column=1, pady=10)

return_box = ttk.Button(root, text="Return", command = return_orders)
return_box.grid(row=8, column=1, pady=10)

finish_btn = ttk.Button(root, text="Quit", command = exit_program)
finish_btn.grid(row=9, column=1, pady=10)


root.mainloop() 
