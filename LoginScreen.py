import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# CODE TO REGISTER NEW USER
# Ask ben how to get it to save the new user info
def register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    label_new_username = tk.Label(register_window, text="New Username:")
    label_new_username.pack(pady=(10,0))
    entry_new_username = tk.Entry(register_window)
    entry_new_username.pack(pady=(0,10))

    label_new_password = tk.Label(register_window, text="New Password:")
    label_new_password.pack(pady=(10,0))
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.pack(pady=(0,10))

    def register_user():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()

        # How to save new user every time?

        messagebox.showinfo("Registration Successful", "Welcome, " + new_username + "!")
        register_window.destroy()

    register_button = tk.Button(register_window, text="Register", command=register_user)
    register_button.pack(pady=(10,20))



# Create the main window
root = tk.Tk()
root.title("Login Screen")

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

# Start the tkinter event loop
root.mainloop()
