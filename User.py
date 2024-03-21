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

    def registerUser(self):
        # Insert the username and password into the database
        self.conn = sqlite3.connect("user_credentials.db")
        self.cursor = self.conn.cursor()

        sql_query = '''
            INSERT INTO users (username, password) VALUES (?,?)
        '''
        print("Executing SQL Query:", sql_query)
        print("Parameters:", (self.username, self.password))

        self.cursor.execute(sql_query, (self.username, self.password))

        self.conn.commit()
        self.conn.close()

         # Print the data being inserted
        print("Inserting into database - Username:", self.username, "Password:", self.password)

        # Execute the SQL query
        self.cursor.execute('''
            INSERT INTO users (username, password) VALUES (?,?)
        ''', (self.username, self.password))

    def authenticate(self):
        # Check if the entered username and password match the ones in the database
        self.conn = sqlite3.connect("user_credentials.db")
        self.cursor = self.conn.cursor()

        sql_query = '''
            SELECT * FROM users
            WHERE username=? AND password=?
        '''
        print("Executing SQL Query:", sql_query)
        print("Parameters:", (self.username, self.password))

        self.cursor.execute(sql_query, (self.username, self.password))

        user_data = self.cursor.fetchone()
        self.conn.close()

        print("User data from database:", user_data)

        return user_data is not None
    


