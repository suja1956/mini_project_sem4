import tkinter as tk
import subprocess


# Define the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x200")
root.configure(bg="pink")

# # Define the admin login page
# admin_page = tk.Toplevel(root)
# admin_page.title("Admin Login")
# admin_page.geometry("300x200")
# admin_page.configure(bg="lightblue")
# admin_page.withdraw()
#
# # Define the user login page
# user_page = tk.Toplevel(root)
# user_page.title("User Login")
# user_page.geometry("300x200")
# user_page.configure(bg="lightgreen")
# user_page.withdraw()

def button_click(button_type):
    if button_type == "admin":
        # Code to navigate to the admin login page
        run_admin_file()
    elif button_type == "user":
        # Code to navigate to the user login page
        run_user_file()

#function to switch to admin login page
def run_admin_file():
    # Run the other Python script
    root.withdraw()
    subprocess.run(["python", "adminLogin.py"])

#function to switch to user login page
def run_user_file():
    # Run the other Python script
    root.withdraw()
    subprocess.run(["python", "userLogin.py"])



# # Define the function to switch to the admin page
# def admin_login():
#     root.withdraw()
#     admin_page.deiconify()
#
# # Define the function to switch to the user page
# def user_login():
#     root.withdraw()
#     user_page.deiconify()

# Define the function to go back to the home page
# def go_home():
#     admin_page.withdraw()
#     user_page.withdraw()
#     root.deiconify()

# Define the buttons in the main window
admin_button = tk.Button(root, text="Admin Login", bg="pink", fg="black", command=lambda: button_click("admin"))
admin_button.pack(pady=20)

user_button = tk.Button(root, text="User Login", bg="pink", fg="black", command=lambda: button_click("user"))
user_button.pack(pady=20)

# Define the back buttons on the login pages
# admin_back_button = tk.Button(admin_page, text="Back", bg="lightblue", fg="black", command=go_home)
# admin_back_button.pack(side="bottom", pady=10)
#
# user_back_button = tk.Button(user_page, text="Back", bg="lightgreen", fg="black", command=go_home)
# user_back_button.pack(side="bottom", pady=10)

root.mainloop()
