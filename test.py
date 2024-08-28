
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="libuser",          # Use the credentials you've configured
        passwd="newpassword",    # Ensure this matches your MySQL user password
        database="Library"       # Use the exact name of the existing database
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

mycursor = mydb.cursor()

# Now you can perform operations directly on the existing tables
mycursor.execute("SELECT * FROM BookRecord")
records = mycursor.fetchall()
for record in records:
    print(record)

# Perform other operations as needed

