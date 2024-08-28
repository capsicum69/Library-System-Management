import mysql.connector
import Tables

def display_books():
    print("\nBook Records:\n")
    db_cursor.execute("""
        SELECT 
            BookRecord.BookID, 
            BookRecord.BookName, 
            BookRecord.Author, 
            BookRecord.Publisher, 
            UserRecord.UserName, 
            UserRecord.UserID
        FROM 
            BookRecord
        LEFT JOIN 
            UserRecord ON BookRecord.BookID = UserRecord.BookID
    """)
    book_records = db_cursor.fetchall()
    for idx, record in enumerate(book_records, start=1):
        print(f"****************************** Row no. {idx} ******************************")
        print(f"\t             BookID: {record[0]}")
        print(f"\t           BookName: {record[1]}")
        print(f"\t             Author: {record[2]}")
        print(f"\t          Publisher: {record[3]}")
        print(f"\t          Issued By: {record[4]}")
        print(f"\t         His UserID: {record[5]}\n")
    input("Press Enter to return to the User Menu")
    return

def insert_book():
    while True:
        print()
        book_id = input("Enter BookID: ")
        book_name = input("Enter Book Name: ")
        author_name = input("Enter Author Name: ")
        publisher_name = input("Enter Publisher Name: ")
        db_cursor.execute("INSERT INTO BookRecord VALUES (%s, %s, %s, %s)", (book_id, book_name, author_name, publisher_name))
        db_connection.commit()
        if input("Do you wish to add more Books?[Yes/No]: ").lower() in {"no"}:
            break
    return

def delete_book():
    while True:
        print()
        book_id = input("Enter BookID whose details to be deleted: ")
        db_cursor.execute("DELETE FROM BookRecord WHERE BookID=%s", (book_id,))
        db_connection.commit()
        if input("Do you wish to delete more Books?[Yes/No]: ").lower() in {"no"}:
            break
    return

def search_book():
    while True:
        print()
        search_id = input("Enter BookID to be Searched: ")
        db_cursor.execute("""
            SELECT 
                BookRecord.BookID, 
                BookRecord.BookName, 
                BookRecord.Author, 
                BookRecord.Publisher, 
                UserRecord.UserName, 
                UserRecord.UserID
            FROM 
                BookRecord
            LEFT JOIN 
                UserRecord ON BookRecord.BookID = UserRecord.BookID
            WHERE 
                BookRecord.BookID=%s
        """, (search_id,))
        book_records = db_cursor.fetchall()
        if book_records:
            for record in book_records:
                print("****************************** Searched Book Record ******************************")
                print(f"\t             BookID: {record[0]}")
                print(f"\t           BookName: {record[1]}")
                print(f"\t             Author: {record[2]}")
                print(f"\t          Publisher: {record[3]}")
                print(f"\t          Issued By: {record[4]}")
                print(f"\t         His UserID: {record[5]}\n")
        else:
            print("Search Unsuccessful")
        if input("Do you wish to search more Books?[Yes/No]: ").lower() in {"no"}:
            break
    return

def update_book():
    while True:
        print()
        book_id = input("Enter Book ID for whose details need to be updated: ")
        book_name = input("Enter updated Book Name: ")
        author_name = input("Enter updated Author Name: ")
        publisher_name = input("Enter the updated Publisher Name: ")
        db_cursor.execute("UPDATE BookRecord SET Bookname = %s, Author = %s, Publisher = %s WHERE BookID = %s", 
                          (book_name, author_name, publisher_name, book_id))
        db_connection.commit()
        print("Updated successfully")
        if input("Do you wish to update more Books?[Yes/No]: ").lower() in {"no"}:
            break
    return

def list_books():
    print("\nBook Records:\n")
    db_cursor.execute("SELECT * FROM BookRecord")
    book_records = db_cursor.fetchall()
    for idx, record in enumerate(book_records, start=1):
        print(f"****************************** Row no. {idx} ******************************")
        print(f"\t             BookID: {record[0]}")
        print(f"\t           BookName: {record[1]}")
        print(f"\t             Author: {record[2]}")
        print(f"\t          Publisher: {record[3]}\n")
    input("Press any key to return to the User Menu")
    return

def issue_book():
    user_id = input("Enter your UserID: ")
    db_cursor.execute("SELECT BookID FROM UserRecord WHERE UserID=%s", (user_id,))
    book_check = db_cursor.fetchone()
    if book_check == (None,):
        print("\nAvailable Books:\n")
        db_cursor.execute("""
            SELECT 
                BookRecord.BookID, 
                BookRecord.BookName, 
                BookRecord.Author, 
                BookRecord.Publisher, 
                UserRecord.UserName, 
                UserRecord.UserID
            FROM 
                BookRecord
            LEFT JOIN 
                UserRecord ON BookRecord.BookID=UserRecord.BookID
        """)
        available_books = db_cursor.fetchall()
        available_books_list = [record for record in available_books if record[5] is None]
        
        if not available_books_list:
            print("Sorry, there are no available books in the Library")
            print("Please wait for some time until someone returns the book you want")
            input("Press any key to return to the User Menu")
            return

        for idx, record in enumerate(available_books_list, start=1):
            print(f"****************************** Row no. {idx} ******************************")
            print(f"\t             BookID: {record[0]}")
            print(f"\t           BookName: {record[1]}")
            print(f"\t             Author: {record[2]}")
            print(f"\t          Publisher: {record[3]}\n")

        user_id = input("Enter your UserID: ")
        issue_book_id = input("Enter the BookID available to be issued: ")
        db_cursor.execute("UPDATE UserRecord SET BookID=%s WHERE UserID=%s", (issue_book_id, user_id))
        db_connection.commit()
        print("Book Successfully Issued")
        input("Press any key to return to the User Menu")
    else:
        print("Book Already Issued, Kindly Return That first")
        input("Press any key to return to the User Menu")
    return

def show_issued_books():
    print()
    user_id = input("Enter your UserID: ")
    db_cursor.execute("""
        SELECT 
            UserID, 
            UserName, 
            UserRecord.BookID, 
            BookName
        FROM 
            Library.UserRecord 
        INNER JOIN 
            Library.BookRecord ON BookRecord.BookID=UserRecord.BookID
        WHERE 
            UserID=%s
    """, (user_id,))
    issued_books = db_cursor.fetchall()
    if issued_books:
        for idx, record in enumerate(issued_books, start=1):
            print(f"****************************** Issued Book ******************************")
            print(f"\t             UserID: {record[0]}")
            print(f"\t           UserName: {record[1]}")
            print(f"\t             BookID: {record[2]}")
            print(f"\t           BookName: {record[3]}\n")
        input("Press any key to return to the User Menu")
    else:
        print("No Book Issued")
        input("Press Enter to return to the User Menu")
    return

def return_book():
    print()
    user_id = input("Enter your UserID: ")
    return_book_id = input("Enter BookID to be returned: ")
    db_cursor.execute("UPDATE UserRecord SET BookID = %s WHERE UserID= %s AND BookID=%s", 
                      (None, user_id, return_book_id))
    db_connection.commit()
    print("Return Successful")
    input("Press Enter to return to the User Menu")
    return

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    passwd="newpassword",
    database="Library"
)
db_cursor = db_connection.cursor()

