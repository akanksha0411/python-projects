# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import os
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

def check_if_entry_exists(file_name, target):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
    except JSONDecodeError or FileNotFoundError:
        print("File is empty, or doesn't exist cannot use json.load(). Just create a file and append your data.")
        return False
    else:
        print(data.keys())
        if target in data.keys():
            print(f"{target} Already Exists")
            return True
        return False

def add_password():
    website_ = website_entry.get()
    username_ = email_entry.get()
    password_ = password_entry.get()

    is_ok = messagebox.askokcancel(title=website_, message= f"These are the details entered: "
                                                            f"\n Email:{username_} \n Password:{password_} \n "
                                                            f"Is it ok to save?")

    info = dict()
    info = {website_ :{
        "Username" : username_,
        "Password" : password_
    }}

    if is_ok:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

        if os.path.isfile("data.json"):
            x = check_if_entry_exists("data.json", website_)
        else:
            with open("data.json", "w") as json_file:
                x = check_if_entry_exists("data.json", website_)
        if x:
            print("Password Already Exists")
            return
        else:
            try:
                with open("data.json", "r") as json_file:
                    data = json.load(json_file)
                    info.update(data)
            except JSONDecodeError:
                print("File is empty, cannot use json.load()")
            finally:
                with open("data.json", "w") as json_file:
                    json.dump(info, json_file, indent=4)
                    print(f"{info} is dumped")

def show_password():
    if toggle_val.get() == 1:
        password_entry.configure(show = "")
    password_entry.configure(show = "*")

def search_password():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    else:
        if website_name in data.keys():
            messagebox.showinfo(title = website_name, message = f"Username: {data[website_name]["Username"]} "
                                                        f"\n Password: {data[website_name]['Password']}")
            print(f"Username: {data[website_name]["Username"]} \n Password: {data[website_name]['Password']}")
        else:
            messagebox.showinfo(f"{website_name} not found.")

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

password_exists = Label(window, text = "Password Already Exists")
password_exists.grid_forget()

website = Label(window, text="Website")
website.grid(row =1, column=0)

username = Label(window, text="Email/Username")
username.grid(row=2, column=0)

password = Label(window, text="Password")
password.grid(row=3, column=0)

website_entry = Entry(window, width = 21)
website_entry.grid(row=1, column=1)

email_entry = Entry(window, width = 35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(window, width = 20, show="*")
password_entry.grid(row=3, column=1)

generate_password = Button(window, text="Generate Password", command=generate_password)
generate_password.grid(row = 3, column = 2)

add_button = Button(window, text ="Add", width=36, command = add_password)
add_button.grid(row = 4, column = 1, columnspan = 2)

add_search = Button(window, text="Search", width=14, command=search_password)
add_search.grid(row = 1, column = 2)

toggle_val = IntVar()
show_password = Checkbutton(window, text = "Show Password", variable= toggle_val, command = show_password)
show_password.grid(row = 5, column = 1)

website_entry.focus()

window.mainloop()
