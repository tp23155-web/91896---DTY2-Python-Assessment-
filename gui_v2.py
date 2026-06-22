
import tkinter as tk
from tkinter import ttk, messagebox

def submit_details(): # on submit gets name, if empty returns error, else prints name and status type
    name = name_entry.get().strip().lower()
    item_status = status_box.get() 
    item = item_entry.get().strip().lower()
    quantity = quantity_entry.get().strip()
    print(name)
    print(item)
    print(quantity)
    print(item_status)

    if name == "":
        messagebox.showerror("Input Error","Name cannot be blank")
        return
    elif item == "":
        messagebox.showerror("Input Error","Item cannot be blank")
        return
    elif quantity == "":
        messagebox.showerror("Input Error","Quantity cannot be blank")
        return
    
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

finish_btn = ttk.Button(root, text="Quit")
finish_btn.grid(row=7, column=1, pady=10)


root.mainloop()
