import Book
import User
import Admin
import Tables
import mysql.connector

def book_management():
    while True:
        print("\t\t\t Book Record Management\n")
        print("==============================================================")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 6-------> : "))
        if choice == 1:
            Book.insert_book()
        elif choice == 2:
            Book.display_books()
        elif choice == 3:
            Book.search_book()
        elif choice == 4:
            Book.delete_book()
        elif choice == 5:
            Book.update_book()
        elif choice == 6:
            return
        else:
            print("Wrong Choice... Enter Your Choice again")
            input("Press Enter to continue")

def user_management():
    while True:
        print("\t\t\t User Record Management\n")
        print("==============================================================")
        print("1. Add User Record")
        print("2. Display User Records")
        print("3. Search User Record")
        print("4. Delete User Record")
        print("5. Update User Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 5-------> : "))
        if choice == 1:
            User.insert_user()
        elif choice == 2:
            User.display_users()
        elif choice == 3:
            User.search_user()
        elif choice == 4:
            User.delete_user()
        elif choice == 5:
            User.update_user()
        elif choice == 6:
            return
        else:
            print("Wrong Choice... Enter Your Choice again")
            input("Press Enter to continue")

def admin_management():
    while True:
        print("\t\t\t Admin Record Management\n")
        print("==============================================================")
        print("1. Add Admin Record")
        print("2. Display Admin Records")
        print("3. Search Admin Record")
        print("4. Delete Admin Record")
        print("5. Update Admin Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 5-------> : "))
        if choice == 1:
            Admin.insert_admin()
        elif choice == 2:
            Admin.display_admin()
        elif choice == 3:
            Admin.search_admin()
        elif choice == 4:
            Admin.delete_admin()
        elif choice == 5:
            Admin.update_admin()
        elif choice == 6:
            return
        else:
            print("Wrong Choice... Enter Your Choice again")
            input("Press Enter to continue")

def feedback_table():
    print("\nFeedback and Rating Table:\n")
    db_cursor.execute("SELECT * from Feedback")
    feedback_records = db_cursor.fetchall()
    for idx, record in enumerate(feedback_records, start=1):
        print(f"****************************** Row no. {idx} ******************************")
        print(f"\t             Feedback: {record[0]}")
        print(f"\t      Rating out of 10: {record[1]}\n")

def book_centre():
    while True:
        print("\t\t\t Book Centre \n")
        print("==============================================================")
        print("1. List of all Books")
        print("2. Issue Book")
        print("3. Display Issued Book Records")
        print("4. Return Issued Book")
        print("5. Return to Main Menu")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 4-------> : "))
        if choice == 1:
            Book.list_books()
        elif choice == 2:
            Book.issue_book()
        elif choice == 3:
            Book.show_issued_books()
        elif choice == 4:
            Book.return_book()
        elif choice == 5:
            return
        else:
            print("Wrong Choice... Enter Your Choice again")
            input("Press Enter to continue")

def feedback():
    while True:
        print("\t\t\t Feedback and Rating\n")
        feedback = input("Enter your Review about our Library and tell us how we can improve: ")
        rating = input("Rate us out of 10: ")
        db_cursor.execute("INSERT INTO Feedback VALUES (%s, %s)", (feedback, rating))
        db_connection.commit()
        print("\nThank you for your valuable Feedback")
        return

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    passwd="newpassword",
    database="Library"
)
db_cursor = db_connection.cursor()

