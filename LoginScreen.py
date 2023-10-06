import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

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
