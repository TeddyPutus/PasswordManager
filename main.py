import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email" : email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="One or more fields are empty!")
        return

    confirmation = messagebox.askyesno(title=f"Password for {website}", message=f"Are these details correct?\nEmail: {email}\nPassword: {password}")

    if confirmation:
        try:
            file = open("data.json", "r")
            data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                file.close()
    pyperclip.copy(password)
    website_input.delete(0, 'end')
    password_input.delete(0, 'end')

#password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, 'end')
    password_input.insert(0, password)

def search_password():
    try:
        file = open("data.json", "r")
        data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No password file!")
    else:
        website = website_input.get()
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}",
                                message=f"Website: {website}\nEmail: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No password for that website!")

#UI Set up
window = tkinter.Tk()
window.title("MyPass")
window.configure(padx=50, pady=50)

#logo
logo_photo = tkinter.PhotoImage(file="logo.png")
logo_canvas = tkinter.Canvas(width=200, height=200)
img = logo_canvas.create_image(100, 100, image=logo_photo)
logo_canvas.grid(row=0, column=1)

#text
website_label = tkinter.Label()
website_label.config(text="Website: ")
website_label.grid(row=1, column=0)

email_label = tkinter.Label()
email_label.config(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = tkinter.Label()
password_label.config(text="Password: ")
password_label.grid(row=3, column=0)

#buttons
generate_button = tkinter.Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=add_password, width=46)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)

#input
website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1)
email_input.insert(0, "teddyputus1@gmail.com")

password_input = tkinter.Entry(width=35)
password_input.grid(row=3, column=1)

window.mainloop()
