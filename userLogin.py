import tkinter as tk
from tkinter import messagebox
import subprocess

# function to validate phone number
def validate_phone_number(phone_number):
    if len(phone_number) != 10 or not phone_number.isdigit():
        messagebox.showerror("Error", "Invalid phone number. Please enter a 10-digit phone number.")
        return False
    return True

def button_click(button_type):
    if button_type == "main":
        # Code to navigate to the user login page
        run_main_file()
    elif button_type == "home":
        # Code to navigate to the user login page
        run_home_file()

def run_home_file():
    window.withdraw()
    subprocess.run(["python", "homePage1.py"])

def run_main_file():
    window.withdraw()
    subprocess.run(["python", "main.py"])

# function to perform login
def login():
    name = name_entry.get()
    phone_number = phone_entry.get()
    if validate_phone_number(phone_number):
        # Perform login action here
        print("Login successful")
        # Clear the input fields after successful login
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        run_main_file()

# create a new tkinter window
window = tk.Tk()

# set the window title
window.title("User Login")

# set the window size
window.geometry("300x200")

# set the window background color
window.configure(bg="pink")

# create a label for name input
name_label = tk.Label(window, text="Name:", bg="pink", fg="black")
name_label.pack()

# create an entry field for name input
name_entry = tk.Entry(window)
name_entry.pack()

# create a label for phone number input
phone_label = tk.Label(window, text="Phone Number:", bg="pink", fg="black")
phone_label.pack()

# create an entry field for phone number input
phone_entry = tk.Entry(window)
phone_entry.pack()

# create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

user_back_button = tk.Button(window, text="Back", bg="lightgreen", fg="black", command=run_home_file)
user_back_button.pack(side="bottom", pady=10)

# run the tkinter window
window.mainloop()
