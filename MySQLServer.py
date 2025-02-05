import mysql.connector

# Database connection details (replace with your own)
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    # database="testdb",
)
my_cursor = my_db.cursor()

# Create a table named `customers` (if it doesn't exist)
my_cursor.execute("""
    CREATE DATABASE IF NOT EXISTS alx_book_store
""")
