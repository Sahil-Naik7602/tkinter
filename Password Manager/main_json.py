from email import message
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_random_password():
    password_list = []
    letter_list =[random.choice(letters) for item in range(nr_letters)]
    char_list =[random.choice(symbols) for item in range(nr_symbols)]
    num_list = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = letter_list + char_list + num_list

    password="".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you havn't left any field empty!")
    else:
        try:
            with open("Passwords_Manager_Directory.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("Passwords_Manager_Directory.json",mode="w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file,indent=4)
                
        else:
            with open("Passwords_Manager_Directory.json",mode="w") as data_file:
                #Updating old data with new data
                data.update(new_data)
                #Saving updated data
                json.dump(data, data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("Passwords_Manager_Directory.json",mode="r") as data_file:
            data=json.load(data_file)
    except :
        messagebox.showinfo(title="error", message="File Not Found")
    else:
        if len(website)==0:
            messagebox.showinfo(title="Oops", message="Please make sure you havn't left any field empty!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error",message=f"This website {website} doesn't exist in the log please either add or check the spelling of the website you added.")
    finally:
        website_entry.delete(0,END)
        




                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1,row=0)

#All Labels---------
website_label = Label(text="Website:")
website_label.grid(column=0,row=1) 
 
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#All entries
website_entry =  Entry(width=17)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2 )
email_entry.insert(0,"sahilnaik7602@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1,row=3)

#All buttons
generate_password_button = Button(text="Generate Password",command=generate_random_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=30,command=add)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=15,command=search)
search_button.grid(column=2,row=1)

window.mainloop()