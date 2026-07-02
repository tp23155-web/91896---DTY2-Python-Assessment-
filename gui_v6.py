import tkinter as tk
from tkinter import ttk, messagebox
import random

final_name = []
item_hired = []
quantity_hired = []
item_receipts = []

def instructions():
    # Instruction prompt at beginning of code being run
    messagebox.showinfo(
        "Instructions",
        "For each set of items hired by a single customer, enter:\n\n"
        "- Customer full name\n"
        "- Specific item\n"
        "- Number of items hired\n\n"
        "When an item is returned, the order will be added to a separate returned section.\n\n"
        "There will be an option to exit the program early, allowing the user to quit if they did not wish to continue, however this will clear the file if orders are placed after close.\n\n"
        "All data will be stored on a separate .txt file for reviewing later."
    )
    
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
    # Converts inputs to variable
    name = name_entry.get().strip().lower()
    item = item_entry.get().strip().lower()
    quantity = quantity_entry.get().strip()
    manual_receipt = receipt_entry.get().strip() 

    # Check for input in boxes
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

    # able to enter receipt manually
    if manual_receipt != "":
        try:
            receipts = int(manual_receipt)
        except ValueError:
            messagebox.showerror("Error", "Manual receipt must be a whole number.")
            return
        
        # Check if the receipt number is already taken
        if receipts in item_receipts:
            messagebox.showerror("Error", f"Receipt number {receipts} already exists. Please choose another.")
            return
    else:
        # Generate a unique random number for receipt if left blank
        while True:
            receipts = random.randint(1, 100000)
            if receipts not in item_receipts:
                break
    
    # Append to lists
    final_name.append(name)
    item_hired.append(item)
    quantity_hired.append(new_quantity)
    item_receipts.append(receipts)
    
    # Save to file
    save_data()

    # Create a list of "Receipt - Name" for the dropdown
    dropdown_list = [f"{item_receipts[i]} - {final_name[i].title()}" for i in range(len(item_receipts))]
    status_box['values'] = dropdown_list
    status_box.set(f"{receipts} - {name.title()}") 
    
    # Clear boxes for next entry
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END) # Clear the receipt entry box
    
    messagebox.showinfo("Success", f"Details added! Receipt: {receipts}")

def return_orders():
    index = status_box.current()

    if index == -1:
        messagebox.showerror("Error", "Please select a receipt to return.")
        return

    receipt = item_receipts[index]

    del final_name[index]
    del item_hired[index]
    del quantity_hired[index]
    del item_receipts[index]
    
    save_data()
    
    dropdown_list = [f"{item_receipts[i]} - {final_name[i].title()}" for i in range(len(item_receipts))]
    status_box['values'] = dropdown_list
    status_box.set("") 
    
    messagebox.showinfo("Success", f"Receipt {receipt} has been removed.")

def exit_program():
    root.quit()

#Visual GUI

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

# Changed name to 'receipt_entry' to avoid conflict with the 'receipt' integer variable
tk.Label(root, text="Receipt (Opt):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
receipt_entry = ttk.Entry(root, width=20)
receipt_entry.grid(row=4, column=1, padx=5, pady=5)

submit_btn = ttk.Button(root, text="Enter Details", command=submit_details)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10)

returns_label = ttk.Label(root, text="Returns", font=("Verdana", 16, "bold"))
returns_label.grid(row=6, column=0, columnspan=2, pady=10)

status_box = ttk.Combobox(root, values=[], state="readonly", width=18)
status_box.grid(row=7, column=0, columnspan=2, pady=5)

return_btn = ttk.Button(root, text="Return Item", command=return_orders)
return_btn.place(x = 35, y = 325)

finish_btn = ttk.Button(root, text="Quit", command=exit_program)
finish_btn.place(x = 150, y = 325)

root.after(100, instructions)
root.mainloop()