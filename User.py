import mysql.connector
import Tables

def display_users():
    print("\nUser Records:\n")
    db_cursor.execute("""
        SELECT 
            UserRecord.UserID, 
            UserRecord.UserName, 
            UserRecord.Password, 
            BookRecord.BookName, 
            BookRecord.BookID
        FROM 
            UserRecord
        LEFT JOIN 
            BookRecord ON UserRecord.BookID=BookRecord.BookID
    """)
    user_records = db_cursor.fetchall()
    for idx, record in enumerate(user_records, start=1):
        print(f"****************************** Row no. {idx} ******************************")
        print(f"\t             UserID: {record[0]}")
        print(f"\t           UserName: {record[1]}")
        print(f"\t           Password: {record[2]}")
        print(f"\t        Book Issued: {record[3]}")
        print(f"\t         Its BookID: {record[4]}\n")
    input("Press any key to return to the User Menu")
    return

def insert_user():
    while True:
        print()
        user_id = input("Enter UserID: ")
        user_name = input("Enter User Name: ")
        password = input("Enter Password to be Set: ")
        db_cursor.execute("INSERT INTO UserRecord VALUES (%s, %s, %s, %s)", (user_id, user_name, password, None))
        db_connection.commit()
        if input("Do you wish to add more Users?[Yes/No]: ").lower() in {"no"}:
            break
    return

def delete_user():
    while True:
        print()
        user_id = input("Enter UserID whose details to be deleted: ")
        db_cursor.execute("DELETE FROM UserRecord WHERE UserID = %s", (user_id,))
        db_connection.commit()
        if input("Do you wish to delete more Users?[Yes/No]: ").lower() in {"no"}:
            break
    return

def search_user():
    while True:
        print()
        search_id = input("Enter UserID to be Searched: ")
        db_cursor.execute("""
            SELECT 
                UserID, 
                UserName, 
                Password, 
                BookName, 
                UserRecord.BookID
            FROM 
                Library.UserRecord 
            LEFT JOIN 
                Library.BookRecord ON BookRecord.BookID=UserRecord.BookID
            WHERE 
                UserRecord.UserID=%s
        """, (search_id,))
        user_records = db_cursor.fetchall()
        if user_records:
            for record in user_records:
                print("****************************** Searched User Record ******************************")
                print(f"\t             UserID: {record[0]}")
                print(f"\t           UserName: {record[1]}")
                print(f"\t           Password: {record[2]}")
                print(f"\t        Book Issued: {record[3]}")
                print(f"\t         Its BookID: {record[4]}\n")
        else:
            print("Search Unsuccessful")
        if input("Do you wish to search more Users?[Yes/No]: ").lower() in {"no"}:
            break
    return

def update_user():
    while True:
        print()
        user_id = input("Enter User ID for whose details need to be updated: ")
        user_name = input("Enter Updated User Name: ")
        password = input("Enter Updated Password: ")
        db_cursor.execute("UPDATE UserRecord SET Username = %s, Password = %s WHERE UserID=%s", 
                          (user_name, password, user_id))
        db_connection.commit()
        print("Updated successfully")
        if input("Do you wish to update more Users?[Yes/No]: ").lower() in {"no"}:
            break
    return

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    passwd="newpassword",
    database="Library"
)
db_cursor = db_connection.cursor()

