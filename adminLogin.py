import tkinter as tk
from tkinter import messagebox
import subprocess

def button_click(button_type):
    if button_type == "main":
        # Code to navigate to the user login page
        run_main_file()
    elif button_type == "home":
        # Code to navigate to the user login page
        run_home_file()

def run_home_file():
    root.withdraw()
    subprocess.run(["python", "homePage1.py"])

def run_main_file():
    root.withdraw()
    subprocess.run(["python", "main.py"])

def admin_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin123" and password == "admin":
        # successful login, show message box and move to admin page
        messagebox.showinfo("Login Successful", "Welcome Admin!")
        # code to move to admin page here
        run_main_file()
    else:
        # login failed, show error message
        messagebox.showerror("Login Failed", "Invalid Username or Password")



# create the window
root = tk.Tk()
root.title("Admin Login")
root.geometry("300x200")
root.config(bg="pink")

# create the username label and entry
username_label = tk.Label(root, text="Username:", bg="pink", fg="black")
username_label.pack(pady=10)
username_entry = tk.Entry(root, width=20)
username_entry.pack()

# create the password label and entry
password_label = tk.Label(root, text="Password:", bg="pink", fg="black")
password_label.pack(pady=10)
password_entry = tk.Entry(root, width=20, show="*")
password_entry.pack()

# create the login button
login_button = tk.Button(root, text="Login", command=admin_login)
login_button.pack(pady=10)

user_back_button = tk.Button(root, text="Back", bg="lightgreen", fg="black", command=run_home_file)
user_back_button.pack(side="bottom", pady=10)

root.mainloop()
