# Library Management System

## Project Overview

The **Library Management System** is a Python-based application designed to manage the operations of a library. It allows administrators to manage books, users, and administrative records, while users can issue and return books, and provide feedback about the library. This system uses MySQL as the backend database to store information about books, users, administrators, and feedback.

## Features

### Admin Features:
- **Book Management:** Add, update, delete, and search for books in the library.
- **User Management:** Add, update, delete, and search for library users.
- **Admin Management:** Manage administrator accounts by adding, updating, deleting, and searching for administrators.
- **Feedback Management:** View feedback and ratings provided by users.

### User Features:
- **View Book List:** View the list of all available books in the library.
- **Issue Book:** Issue a book if it is available and not already issued.
- **Return Book:** Return a previously issued book.
- **View Issued Books:** View the list of books currently issued by the user.
- **Provide Feedback:** Submit feedback and ratings about the library.

## Installation and Setup

### Prerequisites
- Python 3.x
- MySQL
- Git (for version control)

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### Step 2: Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install mysql-connector-python
```

### Step 4: Set Up the Database

1. **Log in to MySQL:**
   ```bash
   mysql -u root -p
   ```

2. **Create the Database and Tables:**
   Run the `Tables.py` script to create the necessary database and tables:
   ```bash
   python Tables.py
   ```

### Step 5: Running the Application

- To start the application, run the `ProjectLogin.py` file:
  ```bash
  python ProjectLogin.py
  ```

## Usage

### Admin Login
- Use the default admin credentials provided in the `AdminRecord` table:
  - AdminID: `Kunal1020`, Password: `123`
  - AdminID: `Siddesh510`, Password: `786`
  - AdminID: `Vishal305`, Password: `675`

### User Login
- Users can either create an account or log in with existing credentials:
  - UserID: `101`, Password: `1234`
  - UserID: `102`, Password: `3050`
  - UserID: `103`, Password: `5010`

### Admin Operations
- Admins can manage books, users, and other admins through the Admin Menu.

### User Operations
- Users can issue books, return books, view issued books, and provide feedback.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you'd like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the open-source community for providing tools and libraries that made this project possible.

## Reach out

- Reach out regarding any queries at developergarvitpandey@gmail.com

