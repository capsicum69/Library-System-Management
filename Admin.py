import mysql.connector
import Tables

def display_admin():
    print("\nAdmin Records:\n")
    db_cursor.execute("SELECT * FROM AdminRecord")
    admin_records = db_cursor.fetchall()
    for idx, record in enumerate(admin_records, start=1):
        print(f"****************************** Row no. {idx} ******************************")
        print(f"\t             AdminID: {record[0]}")
        print(f"\t            Password: {record[1]}\n")
    input("Press Enter to continue")
    return

def insert_admin():
    while True:
        print()
        admin_id = input("Enter AdminID: ")
        admin_password = input("Enter Password to be set: ")
        db_cursor.execute("INSERT INTO AdminRecord VALUES (%s, %s)", (admin_id, admin_password))
        db_connection.commit()
        if input("Do you wish to add more Administrators?[Yes/No]: ").lower() in {"no"}:
            break
    return

def delete_admin():
    while True:
        print()
        admin_id = input("Enter AdminID whose details to be deleted: ")
        db_cursor.execute("DELETE FROM AdminRecord WHERE AdminID=%s", (admin_id,))
        db_connection.commit()
        if input("Do you wish to delete more Administrators?[Yes/No]: ").lower() in {"no"}:
            break
    return

def search_admin():
    while True:
        print()
        search_id = input("Enter AdminID to be Searched: ")
        db_cursor.execute("SELECT * FROM AdminRecord WHERE AdminID=%s", (search_id,))
        admin_records = db_cursor.fetchall()
        if admin_records:
            for record in admin_records:
                print("****************************** Searched Admin Record ******************************")
                print(f"\t             AdminID: {record[0]}")
                print(f"\t            Password: {record[1]}\n")
        else:
            print("Search Unsuccessful")
        if input("Do you wish to search more Administrators?[Yes/No]: ").lower() in {"no"}:
            break
    return

def update_admin():
    while True:
        print()
        admin_id = input("Enter Admin ID for whose details need to be updated: ")
        new_password = input("Enter new Password: ")
        db_cursor.execute("UPDATE AdminRecord SET Password = %s WHERE AdminID=%s", (new_password, admin_id))
        db_connection.commit()
        if input("Do you wish to update more Administrators?[Yes/No]: ").lower() in {"no"}:
            break
    return

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    passwd="newpassword",
    database="Library"
)
db_cursor = db_connection.cursor()

