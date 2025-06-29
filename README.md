#  Admin Login & Student Database Management System
> **Learning / Demo Project:** Developed as part of my learning journey to practice Python file I/O, user authentication, and CRUD operations.
A **terminal-based Python application** that provides secure admin login functionality and a full-featured Student Database Management System. All data is stored in a CSV file and managed using Python’s standard libraries.
> devloped for : class 12th CS EndTerm Lab project
---

##  Features
###  Admin Login System
- Secure admin authentication using username and password
- Password input hidden via `getpass` module
- Maximum 3 login attempts before exit

###  Student Database Management System
- Add new student records with multiple fields
- View all student entries in a clean tabular format
- Search for students by roll number
- Update existing student information
- Delete student entries
- Data persistence via CSV file (`students.csv`)

---

Learning Outcomes:
- Practice reading from and writing to CSV files using Python’s `csv` module.
- Implement basic user authentication with hidden password entry (`getpass`).
- Design a simple menu-driven CRUD (Create, Read, Update, Delete) interface.
- Structure a small terminal application with separation of concerns.
- Understand data persistence in a flat-file system.
- 
---
##  Technologies Used

| Technology  | Purpose                           |
|-------------|-----------------------------------|
| Python 3    | Core programming language         |
| `csv`       | Read/write data to CSV files      |
| `getpass`   | Hide password input in terminal   |

---

##  Files Used

| File Name      | Description                                                     |
|----------------|-----------------------------------------------------------------|
| `main.py`      | Main Python script containing login and database logic          |
| `students.csv` | CSV file storing student records (auto-generated on first run)  |

---

## 🧪 How to Run the Project

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/student-db-admin-system.git
   cd student-db-admin-system

2. No external libraries needed; uses Python standard library.
3. Run the main script:
  bash
  Copy
  Edit
  python main.py
  Login as Admin:
  Use any of the sample credentials above or add your own.

---

## Limitations:
- Passwords are stored in **plain text** inside the CSV file.
- No input validation (e.g., email format, phone number length).
- No role-based access control – any valid user acts as “admin.”
- CSV storage is not thread- or transaction-safe; not suitable for concurrent users.
- Terminal-only interface; no GUI or web frontend.
  
---

## Scope for Improvements:
1. **Password Encryption**: Hash passwords with `hashlib` or `bcrypt` before saving.
2. **Input Validation**: Use regex to validate emails, phone numbers, and numeric fields.
3. **Database Backend**: Migrate from CSV to SQLite or another RDBMS.
4. **GUI/Web Interface**: Build a desktop GUI (Tkinter/PyQt) or web app (Flask/Django).
5. **Role Management**: Introduce user roles (admin vs. student) with different permissions.
6. **Logging & Auditing**: Record all admin actions to a log file for traceability.
7. **Pagination & Search**: Implement pagination and advanced search/filtering for large datasets.
   
---

## References:
- [Youtube](https://www.youtube.com/watch?v=9OjD_HjV03E)
- [Medium](https://rs-punia.medium.com/designing-a-login-register-and-user-authentication-script-in-python-326a11821504)  
- [Random modules](https://www.w3schools.com/python/module_random.asp)
- [Random modules](https://www.geeksforgeeks.org/python-random-module/)

---
### If you found this helpful, feel free to explore the repo and suggest improvements!

