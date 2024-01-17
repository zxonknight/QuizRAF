
# -----------------------------------------------------------------------------------------------------------------------
# USER.PY 
# -----------------------------------------------------------------------------------------------------------------------

import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Create a connection to database
        self.conn = sqlite3.connect("user_credentials.db") 
        #Get the cursor of the database
        self.cursor = self.conn.cursor()
        #execute the command in sql
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
        #
        self.conn.commit()
        self.conn.close()

    def registerUser():
        #we are goning to  INSERT the username and password into the database
        # Create a connection to database
        self.conn = sqlite3.connect("user_credentials.db") 
        #Get the cursor of the database
        self.cursor = self.conn.cursor()
        #execute the command in sql
        self.cursor.execute('''
        INSERT INTO user (username, password) VALUES (?,?)
        ''', (self.username, self.password))
        #
        self.conn.commit()
        self.conn.close()

      def authenticate(self):
        # Check if the entered username and password match the ones in the database
        self.conn = sqlite3.connect("user_credentials.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            SELECT * FROM users
            WHERE username=? AND password=?
        ''', (self.username, self.password))

        user_data = self.cursor.fetchone()
        self.conn.close()

        return user_data is not None
    
