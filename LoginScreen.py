# Imports the tkinter module for GUI development and message box for pop-up messages
import tkinter as tk
from tkinter import messagebox

# Defines the User class to represent a user with a username and password
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# login process
def login():
    # Retrieves the entered username and password from the login entry boxes
    username = entry_username.get()
    password = entry_password.get()

    # Checks if the entered credentials match the predefined admin credentials
    if username == "admin" and password == "adminpassword":
        # Displays a pop-up message for successful login as admin
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        # Displays an error pop-up for unsuccessful login attempts
        messagebox.showerror("Login Failed", "Invalid username or password")

# Handles the registration process
def register():
    # Retrieves the entered new username and password from the registration entry boxes
    username = entry_new_username.get() if entry_new_username else ""
    password = entry_new_password.get() if entry_new_password else ""

    # Placeholder logic for the user registration; outputs the new user information
    print("Registered User:")
    print("Username:", username)
    print("Password:", password)

    # Displays a pop-up message for successful registration
    messagebox.showinfo("Registration Successful", "Welcome, " + username + "!")
    
    # Closes the registration window
    register_window.destroy()

# Creates the main window for the login screen
root = tk.Tk()
root.title("Login Screen")
root.geometry("400x300")  # Defines the dimensions of the main window

# Creates labels and entry boxes for the login
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=(10, 0))
entry_username = tk.Entry(root)
entry_username.pack(pady=(0, 10))

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=(0, 10))

# Creates a login button and registers the login function
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=(10, 20))

# Creates a button to trigger the user registration process and registers the register function
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=(10, 20))

# Placeholder variables for the registration window and entry boxes
register_window = None
entry_new_username = None
entry_new_password = None

# Defines the function to create the registration window
def register_window_func():
    global register_window, entry_new_username, entry_new_password

    # Creates a new window for registration
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    # Creates labels and entry boxes for the new username
    label_new_username = tk.Label(register_window, text="New Username:")
    label_new_username.pack(pady=(10, 0))
    
    entry_new_username = tk.Entry(register_window)
    entry_new_username.pack(pady=(0, 10))

    # Creates labels and entry boxes for the new password
    label_new_password = tk.Label(register_window, text="New Password:")
    label_new_password.pack(pady=(10, 0))
    
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.pack(pady=(0, 10))

    # Creates a button to trigger the user registration process and registers the register function
    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.pack(pady=(10, 20))

# Creates a button to trigger the registration window creation
register_button = tk.Button(root, text="Register", command=register_window_func)
register_button.pack(pady=(10, 20))

# Starts the tkinter event loop
root.mainloop()
