<div align="center">

## Academic Record Management System  
### Python | CLI | CRUD-Based Record Handling  

---

</div>

 
 # 📘 Academic Record Management System

## 📌 Overview
The **Student Record Management System** is a beginner-friendly yet practical **Python CLI application** designed to help users manage essential student information efficiently.  
By using a simple text-based interface, this project allows users to handle student data such as **Name**, **Course**, **CGPA**, and **State** in an organized manner. A web-based application to manage student academic records - including CGPA, SGPA, attendance, and course-wise marks. Designed for students, faculty, or academic advisors to easily add, view, update, and delete records.
It also serves as an excellent learning project for anyone looking to understand and practice core Python concepts including **functions**, **loops**, **dictionaries**, **condition checks**, and **interactive user input handling**.

This project is lightweight, easy to run, and perfect for students, educators, and developers exploring their first steps into Python-based data management systems. 

---


## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
- [How to Use](#how-to-use)
- [Screenshots](#screenshots)
- [Assumptions & Limitations](#assumptions--limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)



## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend:** PHP 7+
- **Database:** MySQL
- **Server:** XAMPP / WAMP / LAMP

  Python’s readability and flexibility make it ideal for building simple and interactive management systems like this one



## ⭐ Key Features
- ➕ **Add Student:** Register a new student with detailed information (name, roll number, subject marks, attendance, SGPA, CGPA)/
- 🔍 **Search Student:** Find any student using their unique registration number.
- View all records in a sortable table
- ✏️ **Update Existing Records:** Modify existing student information without re-entering all fields.  
- 🗑️ **Delete Record:** Remove a student’s data when it’s no longer needed.  
- 📋 **Display All Students:** View every stored student record in a clean, readable format.  
- 🖥️ **User-Friendly CLI:** Simple menu-driven interface that guides users step-by-step.
- Simple and responsive UI using Bootstrap
- PHP backend with MySQL database


These features together create a smooth and intuitive experience, even for first-time users.


---

**Steps to Install & Run the Project** 1. 

1. Clone the repository:

git clone https://github.com/PariRaghuwanshi1906/Academic-Record-Management-System.git


2. Navigate to the project directory:

cd Academic-Record-Management-System


3. Run the application:

python "academic record management.py"

**Instructions for Testing**
After running the script, the main menu will appear with the following options:

1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display All Students
6. Exit

## Recommended steps for testing:
1. Add multiple sample students
2. Search for a student using registration number
3. Update specific fields such as course or CGPA
4. Delete a record and confirm removal
5. Display all student records to verify data formatting
6. Exit the application and re-run if required
   
These steps ensure all CRUD operations function correctly.

Ensure Python 3 is installed on your system before running the script.

## 📄 Additional Notes

This project is especially valuable for:

🎓 Students learning Python fundamentals

🧑‍💻 Beginners practicing program logic and file-free data management

🧪 Those exploring small-scale CLI applications

📚 Academic assignments, demonstrations, or workshops

It lays the foundation for more advanced systems that may include file handling, databases, GUIs, or web interfaces


**Screenshots**

```
1) Main Menu
──────────────────────────────────────────────
            STUDENT RECORD MANAGEMENT
──────────────────────────────────────────────
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display All Students
6. Exit
──────────────────────────────────────────────
Enter your choice: _


2) Adding a Student
──────────────────────────────────────────────
                ADD NEW STUDENT
──────────────────────────────────────────────
Enter Registration Number : 101
Enter Name                : Priya Sharma
Enter Course              : B.Tech CSE
Enter CGPA                : 8.9
Enter State               : Madhya Pradesh
──────────────────────────────────────────────
Student record added successfully.


3) Searching for a Student
──────────────────────────────────────────────
                 SEARCH STUDENT
──────────────────────────────────────────────
Enter Registration Number : 101

Record Found:
──────────────────────────────────────────────
Registration Number : 101
Name                : Priya Sharma
Course              : B.Tech CSE
CGPA                : 8.9
State               : Madhya Pradesh
──────────────────────────────────────────────


4) Updating a Student Record
──────────────────────────────────────────────
                 UPDATE RECORD
──────────────────────────────────────────────
Enter Registration Number : 101

Select the field to update:
1. Name
2. Course
3. CGPA
4. State
──────────────────────────────────────────────
Enter your choice: 2
Enter new Course: B.Tech AI & DS
──────────────────────────────────────────────
Record updated successfully.


5) Deleting a Student
──────────────────────────────────────────────
                 DELETE RECORD
──────────────────────────────────────────────
Enter Registration Number : 101
Record deleted successfully.
──────────────────────────────────────────────


6) Displaying All Students
──────────────────────────────────────────────
               ALL STUDENT RECORDS
──────────────────────────────────────────────

Reg No : 101
Name   : Priya Sharma
Course : B.Tech CSE
CGPA   : 8.9
State  : Madhya Pradesh
──────────────────────────────────────────────

Reg No : 102
Name   : Aditya Verma
Course : BCA
CGPA   : 8.2
State  : Rajasthan
──────────────────────────────────────────────


7) Exit Message
──────────────────────────────────────────────
Exiting the program...
Thank you for using the Student Record Management System.
──────────────────────────────────────────────
```

## Future Enhancements
Potential upgrades include:
1. File handling or database integration for permanent storage
2. Graphical interface using Tkinter or PyQt
3. Web-based version using Flask or Django
4. Data export to CSV/JSON
5. Input validation and error handling
6. Modularized code structure
