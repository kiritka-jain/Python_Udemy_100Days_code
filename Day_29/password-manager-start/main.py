from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

password_dict = {}


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    total_letters = random.randint(4, 8)
    total_symbols = random.randint(1, 3)
    total_numbers = random.randint(0, 4)
    password_letter = [random.choice(letters) for _ in range(total_letters)]
    password_numbers = [random.choice(numbers) for _ in range(total_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(total_symbols)]

    pasword_char = password_letter + password_numbers + password_symbols
    random.shuffle(pasword_char)
    password_string = ''
    for character in pasword_char:
        password_string += str(character)
    password_entry.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    generated_password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': generated_password
        }
    }
    if website == '' or generated_password == '':
        messagebox.showerror(title="field not filled", message='You have not entered the complete '
                                                               'details, please fill them before proceeding ')

    else:
        try:
            with open("password_manager.json", mode='r') as password_file:
                # reading the file
                data = json.load(password_file)
        except FileNotFoundError:
            with open("password_manager.json", mode='w') as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            # upadting the data
            data.update(new_data)

            with open("password_manager.json", mode='w') as password_file:
                # saving updated file
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open('password_manager.json', mode='r') as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error:',message='This file does not exist.')
    else:
        if website in data:
            email = data[website]['email']
            corres_password = data[website]['password']
            messagebox.showinfo(title=website, message=f"email:{email}\npassword:{corres_password}")
        else:
            messagebox.showinfo(title='Error',message='Password information for this site does not exist in the data.')


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
website_entry.config(width=21)
website_entry.grid(column=1, row=1)
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
gen_password = Button(text='Generate Password', command=password_generator)
gen_password.grid(column=2, row=3)

# Search Button
search_button = Button(text='Search', width=13, command=search_password)
search_button.grid(column=2, row=1)

# Add Button
add_button = Button(text='Add', command=save_password)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
