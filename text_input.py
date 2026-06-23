def check_inputs(quantity):
    if isinstance(quantity, float):
        return -1 
    try:
        new_quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer (ie: a number which does not have a decimal point).")
        
   

        
