import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Party Hire Shop")
root.geometry ("300x300")

title_label = ttk.Label(root, text="Party Hire Shop", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=1, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = ttk. Entry(root, width= 25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Item: "). grid(row=2, column=0, sticky="e")
age_entry= ttk.Entry(root, width=25)
age_entry.grid(row=2, column =1)

ttk.Label(root, text="Quantity"). grid(row=3, column=0, sticky="e")
age_entry= ttk.Entry(root, width=25)
age_entry.grid(row=3, column =1)


ttk.Label(root, text= "Hired/Returned"). grid(row=4, column=0, sticky="e")
pay_method_box = ttk.Combobox(root, values = ["Hired", "Returned"], state = "readonly")
pay_method_box.grid(row=4, column=1)
pay_method_box.current(0)

submit_btn = ttk.Button(root, text= "Enter Details")
submit_btn.grid(row=5, column=1, pady=10)

finish_btn = ttk.Button(root, text="Quit")
finish_btn.grid(row=7, column=1, pady=10)


root.mainloop()
