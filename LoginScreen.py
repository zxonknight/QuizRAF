# Imports the tkinter module for GUI development and message box for pop-up messages
import tkinter as tk
from tkinter import messagebox

# Imports user
from User import User #Imports the user class from user.py

 # Import the Queue class from the queue module
from queue_class import Queue

# Dictionary to store quiz questions and options
quiz_questions = {
    "RAF People": [
        ("Who is CAS?", ("Rich Knighton", "Mike Andrews")),
        ("Who is Air + Space Cdr?", ("Harv Smyth", "Jane Doe")),
        ("Who is DCAS?", ("Paul Lloyd", "Alice Johnson")),
        ("Who is AOC 22 Gp?", ("Cab Townsend", "Tom Brown")),
        ("Who is WO RAF?", ("Subby Subramanium", "Chris Wilson")),
    ],
    "Pilot Questions": [
        ("What is the opposite of North?", ("South", "East")),
        ("Do you need polarised or unpolarised sunglasses?", ("Unpolarised", "Polarised")),
        ("What is the name of the RAF's jet trainer?", ("Hawk", "Tornado")),
        ("What is mach?", ("Speed of Sound", "Light Speed")),
        ("What is the nickname of the RAFAT?", ("Red Arrows", "Blue Angels")),
    ],
    "RAF Knowledge": [
        ("What does RAF stand for?", ("Royal Air Force", "Royal Army Force")),
        ("When was the RAF founded?", ("1918", "1945")),
        ("How many RAF groups are there?", ("5", "3")),
        ("What group is RAF training?", ("22 Gp", "15 Gp")),
        ("True or False. The RAF is the world's first independent Air Force?", ("True", "False")),
    ],
}


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
    label_quiz_menu = tk.Label(quiz_menu_window, text=f"Welcome, {username}. Select a quiz to get started!")
    label_quiz_menu.pack(pady=10)

    # Button to select RAF People quiz
    btn_raf_people = tk.Button(quiz_menu_window, text="RAF People", command=lambda: start_new_quiz(username, "RAF People"))
    btn_raf_people.pack(pady=5)

    # Button to select Pilot Questions quiz
    btn_pilot_questions = tk.Button(quiz_menu_window, text="Pilot Questions", command=lambda: start_new_quiz(username, "Pilot Questions"))
    btn_pilot_questions.pack(pady=5)

    # Button to select RAF Knowledge quiz
    btn_raf_knowledge = tk.Button(quiz_menu_window, text="RAF Knowledge", command=lambda: start_new_quiz(username, "RAF Knowledge"))
    btn_raf_knowledge.pack(pady=5)


    # Button to exit the application
    btn_exit = tk.Button(quiz_menu_window, text="Exit", command=quiz_menu_window.destroy)
    btn_exit.pack(pady=10)

    # Start the tkinter event loop for the quiz menu window
    quiz_menu_window.mainloop()

# Function to handle starting a new quiz
def start_new_quiz(username, category):
    global quiz_question_window
    # Initialize the queue for the selected category
    initialize_queue(category)

    # Call display_question to display the first question
    display_question()

# Global variable to store the current question
current_question = None

# Function to display a question and options
def display_question():
    global current_question
    # Check if there are questions in the queue
    if not q.is_empty():
        # Get the next question from the queue
        current_question = q.dequeue()
        category, question, options = current_question

        # Create a new window for the quiz question
        global quiz_question_window
        quiz_question_window = tk.Toplevel()
        quiz_question_window.title("Quiz Question")
        quiz_question_window.geometry("400x200")

        # Display the quiz question
        label_question = tk.Label(quiz_question_window, text=question)
        label_question.pack(pady=10)

        # Create buttons for each option
        for option in options:
            btn_option = tk.Button(quiz_question_window, text=option, command=lambda opt=option: answer_selected(opt))
            btn_option.pack(pady=5)
    else:
        # Display a message if the queue is empty
        messagebox.showinfo("Quiz Complete", "No more questions available!")
        # Reset the queue for potential restart of the quiz
        initialize_queue()

# Function to initialize the queue for the selected category
def initialize_queue(category=None):
    global q
    # Clear the queue
    q = Queue()

    # Initialize the queue with questions and options for the selected category
    if category in quiz_questions:
        for question, options in quiz_questions[category]:
            q.enqueue((category, question, options))
    else:
        messagebox.showerror("Error", f"Category '{category}' not found.")

# Function to handle the user's answer selection
def answer_selected(selected_option):
    # Outputs the question and selected option to the terminal
    print(f"Selected Option: {selected_option}")

    # Close the question window
    quiz_question_window.destroy()

    # Display the next question or end the quiz if there are no more questions
    display_question()



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

# Using now
# Create a global queue to store quiz questions and options
q = Queue()

# Initialize the quiz questions and options in the global queue
for category, questions_and_options in quiz_questions.items():
    for question, options in questions_and_options:
        q.enqueue((category, question, options))

# Declares quiz_question_window as a global variable
quiz_question_window = None

# OLD START NEW QUIZ FUNCTION -------------------------------------------------
# Function to handle starting a new quiz
#def start_new_quiz():
 #   global quiz_question_window  # Declares quiz_question_window as a global variable attempt again
  #  # Check if there are questions in the queue
   # if not q.is_empty():
    #    # Get the next question from the queue
     #   category, question, options = q.dequeue()

      #  # Create a new window for the quiz question
       # quiz_question_window = tk.Toplevel(root)
        #quiz_question_window.title("Quiz Question")
        #quiz_question_window.geometry("400x200")

        # Display the quiz question and options
        #label_question = tk.Label(quiz_question_window, text=question)
        #label_question.pack(pady=10)

        # Create buttons for each option
        #for option in options:
        #    btn_option = tk.Button(quiz_question_window, text=option, command=lambda opt=option: answer_selected(category, question, opt))
        #    btn_option.pack(pady=5)


   # else:
        # Display a message if the queue is empty
    #    messagebox.showinfo("Quiz Complete", "No more questions available!")

    # NO LONGER USED
    # Function to handle the user's answer selection
#def answer_selected(category, question, selected_option):
    # Declare quiz_question_window as a global variable to make it accessible from both start_new_quiz and answer_selected functions
  #  global quiz_question_window
    # Outputs the category question and selected option to the terminal
  #  print(f"Category: {category}, Question: {question}, Selected Option: {selected_option}")

    # Close the question window
 #   quiz_question_window.destroy()
    
    # Call start_new_quiz again to proceed to the next question
 #  start_new_quiz()




# Starts the tkinter event loop
root.mainloop()


