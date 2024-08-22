from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pwd_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_input.get()
    email = email_input.get()
    pwd = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": pwd,
        }
    }
    if len(website)==0 or len(pwd)==0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")
    else:
        try:
            with open("file1.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("file1.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data
            data.update(new_data)
            with open("file1.json", "w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)
                # data_file.write(f"{website} | {email} | {pwd}\n ")

        finally:
            web_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search = web_input.get()
    try:
        with open("file1.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if search in data:
            email = data[search]["email"]
            password = data[search]["password"]
            messagebox.showinfo(title=search, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(pady=75,padx=75)

canvas =Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
web_input = Entry(width=33)
web_input.grid(row=1,column=1)
web_input.focus()
email_input = Entry(width=53)
email_input.insert(0, string="mugdhathoke0909@gmail.com")
email_input.grid(row=2,column=1,columnspan = 2)
password_input = Entry(width=33)
password_input.grid(row=3,column=1)

#Buttons
generate_button = Button(text="Generate Password",command=pwd_gen)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add", width=45 ,command=save)
add_button.grid(row=4,column=1,columnspan = 2)
search_button = Button(text="Search", width=16,command=find_password)
search_button.grid(row=1,column=2)





window.mainloop()