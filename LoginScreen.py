import tkinter as tk
from tkinter import messagebox
from User import User

# Creates the main window named login screen
root = tk.Tk()
root.title("Login Screen")

# Sets the size of the main window
root.geometry("400x300")  # You can adjust the dimensions as needed

# Creates entry widgets for username and password
entry_username = tk.Entry(root, width=30)  # Set the width of the username entry
entry_password = tk.Entry(root, show="*", width=30)  # Set the width of the password entry

# Places the entry widgets in the window
entry_username.grid(row=0, column=1, padx=10, pady=10)  # Adjust padx and pady as needed
entry_password.grid(row=1, column=1, padx=10, pady=10)  # Adjust padx and pady as needed

def login():
    username = entry_username.get()
    password = entry_password.get()
    newUser = User(username,password)
    if username == "admin" and password == "adminpassword":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register(username, password):
    newuser = User(username, password)

# CODE TO REGISTER NEW USER
def register_window():
    # Creates a new window for registration
    register_window = tk.Toplevel(root)
    register_window.title("Register")  # Names the window register

    # Creates a label for a new username
    label_new_username = tk.Label(register_window, text="New Username:")
    label_new_username.pack(pady=(10,0))  # Sets the position

    # Create an entry field for the new username
    entry_new_username = tk.Entry(register_window)
    entry_new_username.pack(pady=(0,10))  # sets the position

    # Creates a label for a new password
    label_new_password = tk.Label(register_window, text="New Password:")
    label_new_password.pack(pady=(10,0))  # sets the position

    # Create an entry field for the new password where the typed letters are shown as an astrix (*)
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.pack(pady=(0,10))  # Sets the position
    # Create a button to trigger the user registration process

    username = entry_new_username.get()
    password = entry_new_password.get()

    print(username)
    print(password)

    register_button = tk.Button(register_window, text="Register", command=partial(register, username, password))
    register_button.pack(pady=(10,20))  #Sets the position

def register_user():
    # Get the text entered in the username and password entry fields
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()

    # ** Ask ben how to get it to save the new user info **

    # Display a pop-up message indicating successful registration
    messagebox.showinfo("Registration Successful", "Welcome, " + new_username + "!")
    # Close the registration window
    register_window.destroy()






# Create labels and entry widgets
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=(10,0))
entry_username = tk.Entry(root)
entry_username.pack(pady=(0,10))

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(10,0))
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=(0,10))

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=(10,20))

# Create a button to trigger the user registration process
register_button = tk.Button(root, text="Register", command=register_window)
register_button.pack(pady=(10,20))  #Sets the position
# Start the tkinter event loop
root.mainloop()
