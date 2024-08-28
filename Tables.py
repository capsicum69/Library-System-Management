import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    password="newpassword",
    database="Library"
)

db_cursor = db_connection.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS Library")
db_cursor.execute("USE Library")

db_cursor.execute("SHOW TABLES LIKE 'BookRecord'")
if not db_cursor.fetchone():
    db_cursor.execute("""
        CREATE TABLE BookRecord(
            BookID VARCHAR(10) PRIMARY KEY, 
            BookName VARCHAR(35), 
            Author VARCHAR(30), 
            Publisher VARCHAR(30)
        )
    """)

db_cursor.execute("SHOW TABLES LIKE 'UserRecord'")
if not db_cursor.fetchone():
    db_cursor.execute("""
        CREATE TABLE UserRecord(
            UserID VARCHAR(10) PRIMARY KEY, 
            UserName VARCHAR(20),
            Password VARCHAR(20), 
            BookID VARCHAR(10),
            FOREIGN KEY (BookID) REFERENCES BookRecord(BookID)
        )
    """)
    db_cursor.executemany("INSERT INTO UserRecord VALUES(%s, %s, %s, %s)", [
        ("101", "Kunal", "1234", None),
        ("102", "Vishal", "3050", None),
        ("103", "Siddhesh", "5010", None)
    ])
    db_connection.commit()

db_cursor.execute("SHOW TABLES LIKE 'AdminRecord'")
if not db_cursor.fetchone():
    db_cursor.execute("""
        CREATE TABLE AdminRecord(
            AdminID VARCHAR(10) PRIMARY KEY, 
            Password VARCHAR(20)
        )
    """)
    db_cursor.executemany("INSERT INTO AdminRecord VALUES(%s, %s)", [
        ("Kunal1020", "123"),
        ("Siddesh510", "786"),
        ("Vishal305", "675")
    ])
    db_connection.commit()

db_cursor.execute("SHOW TABLES LIKE 'Feedback'")
if not db_cursor.fetchone():
    db_cursor.execute("CREATE TABLE Feedback(Feedback VARCHAR(100) PRIMARY KEY, Rating VARCHAR(10))")

