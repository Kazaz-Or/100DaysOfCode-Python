import random
import pyperclip
import tkinter
import json
from tkinter import END
from tkinter import messagebox

from data import letters, symbols, numbers


def generate_pass():
    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    symbols_letters = [random.choice(symbols) for i in range(random.randint(1, 2))]
    numbers_letters = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + symbols_letters + numbers_letters
    random.shuffle(password_list)
    pwd = "".join(password_list)

    pass_entry.insert(0, pwd)
    pyperclip.copy(pwd)


def save():
    website = website_entry.get()
    email = email_entry.get()
    psw = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": psw,
    }}

    if len(website) == 0 or len(email) == 0 or len(psw) == 0:
        messagebox.showinfo(title="Note", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = tkinter.Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_pass_button = tkinter.Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
