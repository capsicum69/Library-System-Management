import Operations

def admin_menu():
    while True:
        print("\t\t\t Admin Menu \n")
        print("==============================================================")
        print("1. Book Management")
        print("2. User Management")
        print("3. Admin Management")
        print("4. User Feedback and Ratings Table")
        print("5. Logout ")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 5-------> : "))
        if choice == 1:
            Operations.book_management()
        elif choice == 2:
            Operations.user_management()
        elif choice == 3:
            Operations.admin_management()
        elif choice == 4:
            Operations.feedback_table()
        elif choice == 5:
            print("Thanks for visiting our Library:))")
            print("Logged out of the system")
            break
        else:
            print("Wrong Choice... Enter Your Choice again")
            continue

def user_menu():
    while True:
        print("\t\t\t User Menu \n")
        print("==============================================================")
        print("1. Book Centre")
        print("2. Feedback and Ratings")
        print("3. Logout ")
        print("===============================================================")
        choice = int(input("Enter Choice between 1 to 3-------> : "))
        if choice == 1:
            Operations.book_centre()
        elif choice == 2:
            Operations.feedback()
        elif choice == 3:
            print("Thanks for visiting our Library:))")
            print("Logged out of the system")
            break
        else:
            print("Wrong Choice... Enter Your Choice again")
            continue

user_menu()

