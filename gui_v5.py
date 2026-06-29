import tkinter as tk
from tkinter import ttk, messagebox
import random

final_name = []
item_hired = []
quantity_hired = []
item_receipts = []

def instructions():
    ('''
     For each set of items hired by a single customer, enter...

     - Customer full name

     - specific item 

     - number of items hired 

     When an item is returned, the order will be added to a seperate returned section:

     There will be an option to exit the program early, allowing the user to quit if they did not wish to continue.

     All data will be stored on a seperate .txt file for reviewing later.
     
     ''')
instructions()

def save_data():
    with open("party_hire.txt", "w") as file:
        file.write("----------------------------------------------------------------------------------------------------\n")
        file.write("Party Hire".center(100)+ "\n")
        file.write("----------------------------------------------------------------------------------------------------\n\n")

        for i in range(len(final_name)):
            file.write(f"Name: {final_name[i]}\n")
            file.write(f"Item: {item_hired[i]}\n")
            file.write(f"Quantity: {quantity_hired[i]}\n")
            file.write(f"Receipt Number: {item_receipts[i]}\n\n")

def submit_details():
    name = name_entry.get().strip().lower()
    item = item_entry.get().strip().lower()
    quantity = quantity_entry.get().strip()

    # Check for Input in Boxes
    if name == "" or item == "" or quantity == "":
        messagebox.showerror("Input Error", "All boxes must be filled out.")
        return

    # check and convert quantity
    try:
        new_quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "For quantity please enter a whole number (integer) without decimals.")
        return

    # Check number boundary cases
    if new_quantity <= 0 or new_quantity > 500:
        messagebox.showerror("Error", "Quantity must be between 1 and 500.")
        return

    # Generate a unique random number for receipt
    receipts = random.sample(range(1, 100000), 1)[0]
    
    # Append to lists
    final_name.append(name)
    item_hired.append(item)
    quantity_hired.append(new_quantity)
    item_receipts.append(receipts)
    
    # Save to file
    save_data()

    # Update the the returns dropdown
    status_box['values'] = item_receipts
    status_box.set(receipts) # Instantly shows the new receipt in the box
    
    # Clear boxes for next entry
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", f"Details added! Receipt: {receipts}")

def return_orders():
    # Read from the receipt dropdown 
    remove_order = status_box.get()

    if remove_order == "":
        messagebox.showerror("Error", "Please select a receipt to return.")
        return
    
    receipt = int(remove_order)

    if receipt in item_receipts:
        index = item_receipts.index(receipt)
        del final_name[index]
        del item_hired[index]
        del quantity_hired[index]
        del item_receipts[index]
        
        save_data()
        
        # Update dropdown list 
        status_box['values'] = item_receipts
        status_box.set("") 
        messagebox.showinfo("Success", f"Receipt {receipt} has been removed.")

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Party Hire Shop")
root.geometry("300x420")

title_label = ttk.Label(root, text="Party Hire Shop", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = ttk.Entry(root, width=20)
name_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(root, text="Item:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
item_entry = ttk.Entry(root, width=20)
item_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(root, text="Quantity:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
quantity_entry = ttk.Entry(root, width=20)
quantity_entry.grid(row=3, column=1, padx=5, pady=5)

submit_btn = ttk.Button(root, text="Enter Details", command=submit_details)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

returns_label = ttk.Label(root, text="Returns", font=("Verdana", 16, "bold"))
returns_label.grid(row=5, column=0, columnspan=2, pady=10)

# Combobox box to hold the receipts
status_box = ttk.Combobox(root, values=[], state="readonly", width=18)
status_box.grid(row=6, column=0, columnspan=2, pady=5)

return_btn = ttk.Button(root, text="Return Item", command=return_orders)
return_btn.grid(row=7, column=0, columnspan=2, pady=5)

finish_btn = ttk.Button(root, text="Quit", command=exit_program)
finish_btn.grid(row=8, column=0, columnspan=2, pady=15)

root.mainloop()