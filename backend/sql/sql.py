import pymssql

# Define your MS SQL connection details (to be filled in)
SERVER = 'your_server'
DATABASE = 'your_database'
PORT = 'your_port'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Function to establish a connection to the database
def get_connection():
    return pymssql.connect(server=SERVER, user=USERNAME, password=PASSWORD, database=DATABASE, port=PORT)

# Function to get all users from the database
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT id, name, age FROM Users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to add a new user to the database
def add_user(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (name, age) VALUES (%s, %d)", (name, age))
    conn.commit()
    conn.close()
