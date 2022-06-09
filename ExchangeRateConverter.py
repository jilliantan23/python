import tkinter, tkinter.messagebox, csv, os

conversion_rates = []

def conversion_msg():
    """Runs a series of commands to validate and convert amounts into respective currencies"""
    inputs = []
    inputs2 = []
    try:
        # Create "conversion.csv" file
        with open("conversion.csv", "w") as file:
            writer = csv.writer(file, lineterminator = "\n")
            header = ["Currency", "Quantity", "Total"]
            writer.writerow(header)
            
        # Retrieve exchange rates for each currency
        with open("exchange_rates.csv", "r") as file:
            reader = csv.reader(file, lineterminator = "\n")
            for line in reader:
                conversion_rate = float(line[1]) # Convert rates into type 'float'
                conversion_rates.append(conversion_rate)
            print(conversion_rates)
            gbp_rate = conversion_rates[0]
            eur_rate = conversion_rates[1]
            cad_rate = conversion_rates[2]
            jpy_rate = conversion_rates[3]
            
        a = GBP_box.get()
        b = EUR_box.get()
        c = CAD_box.get()
        d = JPY_box.get()
        
        # Check if user wishes to convert nothing or if box is empty
        if len(a) == 0:
            a = 0
        if len(b) == 0:
            b = 0
        if len(c) == 0:
            c = 0
        if len(d) == 0:
            d = 0
        
        # Add conversion values into a list
        inputs.append(a)
        inputs.append(b)
        inputs.append(c)
        inputs.append(d)
        print(inputs)
        
        for i in inputs: # Convert values into type 'float' by creating a new list
            inputs2.append(float(i))
        print(inputs2) # Now inputs2 list contains quantity values in type 'float'
        
        # Convert user amounts to each currency
        gbp_conversion = inputs2[0] * gbp_rate
        eur_conversion = inputs2[1] * eur_rate
        cad_conversion = inputs2[2] * cad_rate
        jpy_conversion = inputs2[3] * jpy_rate
        
        total_conversion = gbp_conversion + eur_conversion + cad_conversion + jpy_conversion
        
        # Format and print out total currencies in conversion file
        with open("conversion.csv", "a") as input:
            writer = csv.writer(input, lineterminator = "\n")
            spacer = ["--", "--", "--"]
            total = ["Total", "--", round(total_conversion, 2)]
            writer.writerow(["GBP", inputs2[0], round(gbp_conversion, 2)])
            writer.writerow(["EUR", inputs2[1], round(eur_conversion, 2)])
            writer.writerow(["CAD", inputs2[2], round(cad_conversion, 2)])
            writer.writerow(["JPY", inputs2[3], round(jpy_conversion, 2)])
            writer.writerow(spacer)
            writer.writerow(total)
        
        tkinter.messagebox.showinfo("Complete!", "Conversion report was written to conversion.csv.")
    except:
        tkinter.messagebox.showwarning("Warning!", "Sorry, the report could not be written. Check that only numeric values were entered.")
        
def close():
    """Exits out of the program"""
    global root
    root.destroy()

if os.path.exists("exchange_rates.csv"):
    # Create a GUI
    root = tkinter.Tk()
    root.title("Exchange rate calculator")
    root.configure(bg = "skyblue")

    # GBP Exchange Box
    GBP_label = tkinter.Label(root, text = "GBP:")
    GBP_label.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
    GBP_label.configure(bg = "skyblue")

    GBP_box = tkinter.Entry(root, width = 10)
    GBP_box.grid(row = 0, column = 1, sticky = "w", padx = 5, pady = 5)

    # EUR Exchange Box
    EUR_label = tkinter.Label(root, text = "EUR:")
    EUR_label.grid(row = 0, column = 2, sticky = "w", padx = 5, pady = 5)
    EUR_label.configure(bg = "skyblue")

    EUR_box = tkinter.Entry(root, width = 10)
    EUR_box.grid(row = 0, column = 3, sticky = "w", padx = 5, pady = 5)

    # CAD Exchange Box
    CAD_label = tkinter.Label(root, text = "CAD:")
    CAD_label.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)
    CAD_label.configure(bg = "skyblue")

    CAD_box = tkinter.Entry(root, width = 10)
    CAD_box.grid(row = 1, column = 1, sticky = "w", padx = 5, pady = 5)

    # JPY Exchange Box
    JPY_label = tkinter.Label(root, text = "JPY:")
    JPY_label.grid(row = 1, column = 2, sticky = "w", padx = 5, pady = 5)
    JPY_label.configure(bg = "skyblue")

    JPY_box = tkinter.Entry(root, width = 10)
    JPY_box.grid(row = 1, column = 3, sticky = "w", padx = 5, pady = 5)

    # Convert currency button
    convert_button = tkinter.Button(root, text = "Convert currency", command = conversion_msg)
    convert_button.grid(row = 0, column = 4, sticky = "w", padx = 5, pady = 5)
    convert_button.configure(bg = "lightgreen", width = 15)

    # Close conversion button
    close_button = tkinter.Button(root, text = "Close currency", command = close)
    close_button.grid(row = 1, column = 4, sticky = "w", padx = 5, pady = 5)
    close_button.configure(bg = "tomato", width = 15)

    root.mainloop()
else:
    print("Error! 'exchange_rates.csv' file is missing. Try again.")
