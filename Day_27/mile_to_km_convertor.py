from tkinter import *

windows = Tk()
windows.title("Mile to Kilometer convertor")
windows.minsize(width=300, height=200)
windows.config(padx=30, pady=30)

# Entry
entry = Entry(width=10)
# Add miles you want to convert
entry.insert(END, string="")
# Gets text in entry
entry.grid(column=1, row=0)

# Mile input
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

# is equal to
label_2 = Label(text="is euals to")
label_2.grid(column=0, row=1)

# kilometer
label_3 = Label(text="Kilometers")
label_3.grid(column=2, row=1)


# calculate_button_function
def calculate_kilometers():
    mile_val = float(entry.get())
    km_val = float(round(mile_val * 1.60934,2))
    label_4.config(text= km_val)


# calculate_button
button = Button(text="Calculate", command=calculate_kilometers)
button.grid(column=1, row=2)

# Km output
label_4 = Label(text="")
label_4.grid(column=1, row=1)

windows.mainloop()
