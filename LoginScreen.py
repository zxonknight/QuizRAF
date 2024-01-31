# Imports the tkinter module for GUI development and message box for pop-up messages
import tkinter as tk
from tkinter import messagebox

# Imports user
from User import User #Imports the user class from user.py

# ---- THIS PART REMOVED AS USER CLASS FROM USER.PY IS USED ---
# Defines the User class to represent a user with a username and password
# class User:
#    def __init__(self, username, password):
#        self.username = username
#        self.password = password

# login process
def login():
    # Retrieves the entered username and password from the login entry boxes
    username = entry_username.get()
    password = entry_password.get()

    # Check if the entered credentials match the ones in the database
    user = User(username, password)
    open_quiz_menu(username)

    if user.authenticate():
        # Close the login window
        root.destroy()

        # Open the quiz menu window
        open_quiz_menu(username)
    # else:
        # Displays an error pop-up for unsuccessful login attempts
       #TEMP BLOCK# messagebox.showerror("Login Failed", "Invalid username or password")
        # ------------------------------ DEBUG DEBUG DEBUG ----------------------------------------------------------
    else:
        # Display debug information
        print("Authentication failed for user:", username, password)

        # Displays an error pop-up for unsuccessful login attempts
        messagebox.showerror("Login Failed", "Invalid username or password")

        # Check if the entered credentials match the predefined admin credentials
        if username == "admin" and password == "adminpassword":
            # Display debug information
            print("Admin login attempt")

            # Displays a pop-up message for successful login as admin
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            # Display debug information
            print("Regular user login attempt")

            # Displays an error pop-up for unsuccessful login attempts
            messagebox.showerror("Login Failed", "Invalid username or password") 
    #---------------------------------------------- DEBUG DEBUG DEBUG ------------------------------------------------------   

    # Checks if the entered credentials match the predefined admin credentials
   #if username == "admin" and password == "adminpassword":
    #    # Displays a pop-up message for successful login as admin
     #   messagebox.showinfo("Login Successful", "Welcome, Admin!")
    #else:
     #   # Displays an error pop-up for unsuccessful login attempts
      #  messagebox.showerror("Login Failed", "Invalid username or password")

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

def open_quiz_menu(username):
    # Create the quiz menu window
    quiz_menu_window = tk.Tk()
    quiz_menu_window.title("Quiz Menu")
    quiz_menu_window.geometry("400x300")  # Set the dimensions of the quiz menu window

    # Add quiz menu components and functionalities here
    label_quiz_menu = tk.Label(quiz_menu_window, text=f"Welcome, {username}!")
    label_quiz_menu.pack(pady=10)

    # Button to start a new quiz
    btn_new_quiz = tk.Button(quiz_menu_window, text="New Quiz", command=start_new_quiz)
    btn_new_quiz.pack(pady=10)

    # Button to exit the application
    btn_exit = tk.Button(quiz_menu_window, text="Exit", command=quiz_menu_window.destroy)
    btn_exit.pack(pady=10)
    print ("Quiz exited")

    # Start the tkinter event loop for the quiz menu window
    quiz_menu_window.mainloop()

# Function to handle starting a new quiz
def start_new_quiz():
    # Add code here to handle the logic for starting a new quiz
    print("New quiz started!")


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
    root.geometry("300x250")  # Defines the dimensions of the main window

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


