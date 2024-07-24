from tkinter import *
from tkinter import messagebox
import random
import os
import pyperclip
import string
import json

# -----------------------------CONSTANTS------------------------------------------#
FONT_NAME = "Arial"

# -----------------------------PATH-----------------------------------------------#
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "logo.png")
# file_path = os.path.join(script_dir, "password_data.txt")
file_path = os.path.join(script_dir, "password_data.json")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0,END)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------------ #


def clear_entries():
    website_entry.delete(0, END)
    # email_entry.delete(0,END)
    password_entry.delete(0, END)
    website_entry.focus()


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(
            title="Oops", message=f"Please dont leave any fields empty!")
    else:
        try:
            with open(file_path, mode="r") as file:
                #reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(file_path,mode="w") as file:
                #Saving updated data
                json.dump(new_data,file,indent=4)
        else:
            #Updating with new data 
            data.update(new_data)
            with open(file_path,mode="w") as file:
                #Saving updated data
                json.dump(data,file,indent=4)  
        finally:         
            messagebox.showinfo(title="Success",message=f"added {website} credentials to the Data store")
            clear_entries()
# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(file_path, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}",message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error",message=f"No details for {website} exists.")           
    finally:
        website_entry.delete(0, END)
        website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 10), anchor="w")
website_label.grid(row=1, column=0, sticky="we")

email_username_label = Label(
    text="Email/Username:", font=(FONT_NAME, 10), anchor="w")
email_username_label.grid(row=2, column=0, sticky="we")

password_label = Label(text="Password:", font=(FONT_NAME, 10), anchor="w")
password_label.grid(row=3, column=0, sticky="we")

# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="we")

email_entry = Entry(width=35)
email_entry.insert(0, "vreddy.a3@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="we")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="we")

# Buttons
generate_password_button = Button(text="Generate Password",command=password_generator)
generate_password_button.grid(row=3, column=2, sticky="we")

add_button = Button(text="add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

search_button = Button(text="Search",command=find_password)
search_button.grid(row=1, column=2, sticky="we")

window.mainloop()
