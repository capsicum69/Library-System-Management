import sys
import MainMenu
import Tables
import mysql.connector

def login_to_admin():
    print("\n|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print("\n                              LOGIN TO YOUR ACCOUNT                                    \n")
    print("WARNING: Only three Attempts to login")
    for attempts in range(3):
        admin_id = input("\t  Enter AdminID: ")
        password = input("\t  Enter Password: ")
        db_cursor.execute("SELECT Password FROM AdminRecord WHERE AdminID=%s", (admin_id,))
        result = db_cursor.fetchone()
        if result:
            stored_password, = result
            if stored_password == password:
                print(f"\n\t\t    WELCOME {admin_id} to THE BOOK WORM  \n ")
                MainMenu.admin_menu()
                break
            else:
                print("\t INVALID PASSWORD OR USERNAME! TRY AGAIN ")
                print(f"\t {attempts + 1}st attempt is over \n ")
        else:
            print("\t NO SUCH USERNAME! TRY AGAIN ")
            print(f"\t {attempts + 1}st attempt is over \n ")
    else:
        print("\t Try again later \n ")
        print("\t System off  \n ")
        print("*---------------------------------------------------------------------------------* \n")

def login_to_user():
    print("\n|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print("\n1. CREATE ACCOUNT")
    print("2. LOGIN TO YOUR ACCOUNT")
    choice = int(input("Enter choice-->"))
    if choice == 1:
        user_id = input("Enter your UserID: ")
        user_name = input("Enter your Name: ")
        password = input("Enter Password to be set: ")
        db_cursor.execute("INSERT INTO UserRecord VALUES (%s, %s, %s, %s)", (user_id, user_name, password, None))
        db_connection.commit()
        db_cursor.execute("SELECT UserID FROM UserRecord WHERE UserID=%s", (user_id,))
        if db_cursor.fetchone():
            print("Account successfully created")
        else:
            print("Account already exists")
        login_to_user()
    elif choice == 2:
        print("WARNING: Only three Attempts to login at a time")
        for attempts in range(3):
            user_id = input("\t  Enter UserID: ")
            password = input("\t  Enter Password: ")
            db_cursor.execute("SELECT Password FROM UserRecord WHERE UserID=%s", (user_id,))
            result = db_cursor.fetchone()
            if result:
                stored_password, = result
                if stored_password == password:
                    print(f"\n\t\t    WELCOME {user_id} to THE BOOK WORM  \n ")
                    MainMenu.user_menu()
                    break
                else:
                    print("\t INVALID PASSWORD OR USERNAME! TRY AGAIN ")
                    print(f"\t {attempts + 1}st attempt is over \n ")
            else:
                print("\t NO SUCH USERNAME! TRY AGAIN ")
                print(f"\t {attempts + 1}st attempt is over \n ")
        else:
            print("\t Try again later \n ")
            print("\t System off  \n ")
            print("*---------------------------------------------------------------------------------* \n")
    else:
        print("Enter valid choice")
        login_to_user()

def menu():
    print("\n\n|*************************************************************************************|")
    print("|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print("|*************************************************************************************|")
    print("\n                 ======================= MENU =======================                \n")
    print(" 1. Login as a ADMIN")
    print(" 2. Login as a USER")
    print(" 3. EXIT \n\n ")
    while True:
        choice = input(" Select [ 1/2/3 ] : ")
        if choice == "1":
            login_to_admin()
            break
        elif choice == "2":
            login_to_user()
            break
        elif choice == "3":
            if input(" DO YOU WISH TO EXIT... [yes/no]: ").lower() in ["yes"]:
                sys.exit()
            break
        else:
            print(" INVALID COMMAND ")
            print(" RETRY \n")

db_connection = mysql.connector.connect(
    host="localhost",
    user="libuser",
    passwd="newpassword",
    database="Library"
)
db_cursor = db_connection.cursor()

menu()

