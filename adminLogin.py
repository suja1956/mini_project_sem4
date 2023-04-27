import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import subprocess
from customtkinter import *
def button_click(button_type):
    if button_type == "main":
        # Code to navigate to the user login page
        run_main_file()
    elif button_type == "home":
        # Code to navigate to the user login page
        run_home_file()

def run_home_file():
    root.withdraw()
    subprocess.run(["python", "main.py"])

def run_main_file():
    root.withdraw()
    subprocess.run(["python", "EMS.py"])

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

# # create the username label and entry
# username_label = tk.Label(root, text="Username:", bg="pink", fg="black")
# username_label.pack(pady=10)
# username_entry = tk.Entry(root, width=20)
# username_entry.pack()
#
# # create the password label and entry
# password_label = tk.Label(root, text="Password:", bg="pink", fg="black")
# password_label.pack(pady=10)
# password_entry = tk.Entry(root, width=20, show="*")
# password_entry.pack()
#
# # create the login button
# login_button = tk.Button(root, text="Login", command=admin_login)
# login_button.pack(pady=10)
#
# user_back_button = tk.Button(root, text="Back", bg="lightgreen", fg="black", command=run_home_file)
# user_back_button.pack(side="bottom", pady=10)
set_appearance_mode ("system")
set_default_color_theme("blue")
root = CTk()
root.title("Login Page")
root.geometry("500x400")
frame = CTkFrame(root)
frame.pack(expand=True, fill="both", padx=20, pady=60)
CTkLabel(frame, text ="Admin Login", font=("Roboto", 26)).pack(pady=20)
username_entry = CTkEntry(frame, placeholder_text="username", width=250)
username_entry.pack()
password_entry = CTkEntry(frame, placeholder_text="Password", width=250)
password_entry.pack(pady=15)

CTkButton(frame, text="Login", command=admin_login).pack(padx=20, pady=20)
CTkButton(frame, text="Back", command=run_home_file).pack()
root.mainloop()

