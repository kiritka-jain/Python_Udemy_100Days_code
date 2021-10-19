from tkinter import *
from tkinter import messagebox
import random
import pyperclip

password_dict = {}


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    total_letters = random.randint(4,8)
    total_symbols = random.randint(1,3)
    total_numbers = random.randint(0,4)
    password_letter = [random.choice(letters) for _ in range(total_letters)]
    password_numbers = [random.choice(numbers) for _ in range(total_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(total_symbols)]

    pasword_char = password_letter+password_numbers+password_symbols
    random.shuffle(pasword_char)
    password_string = ''
    for character in pasword_char:
        password_string+=str(character)
    password_entry.insert(0,password_string)
    pyperclip.copy(password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    generated_password = password_entry.get()
    if website == '' or generated_password =='':
        messagebox.showerror(title="field not filled",message='You have not entered the complete '
                                                              'details, please fill them before proceeding ')
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Do you want to save the following "
                                                     f"details?:\n{email}:\n{generated_password}")
        if is_ok:
            with open("password_manager.txt", mode='a') as password_file:
                password_file.write(f"{website} | {email} | {generated_password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

# Website Entry
website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label
username = Label(text='Email/Username:')
username.grid(column=0, row=2)

# Username Entry
username_entry = Entry()
username_entry.config(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'kirtika@gmail.com')

# Password Label
password = Label(text='Password:')
password.grid(column=0, row=3)

# Password Entry
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

# Generate Password Button
gen_password = Button(text='Generate Password',command= password_generator)
gen_password.grid(column=2, row=3)

# Add Button
add_button = Button(text='Add', command=save_password)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
