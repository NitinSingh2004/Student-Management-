# Student Management System

This is a simple Student Management System built using Python, Tkinter for the GUI, and MySQL for database management. The application allows users to add, update, delete, and view student records.

## Features
- Add new students to the database.
- Update existing student records.
- Delete student records.
- View all student details in a table.
- Interactive GUI with Tkinter.

## Requirements
Make sure you have Python installed. You also need MySQL installed and running.

### Install Dependencies
Run the following command to install required packages:
```sh
pip install mysql-connector-python
```

## Database Setup
Before running the application, set up your MySQL database:

1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE student_info;
   ```
2. Select the database:
   ```sql
   USE student_info;
   ```
3. Create the table:
   ```sql
   CREATE TABLE students_rec (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       age INT NOT NULL,
       gender VARCHAR(50) NOT NULL,
       course VARCHAR(255) NOT NULL
   );
   ```

## Running the Application
Run the following command in your terminal or command prompt:
```sh
python student_management.py
```

## Usage
1. Enter student details (Name, Age, Gender, Course).
2. Click **Add** to insert a new record.
3. Select a student from the list to update or delete.
4. Click **Update** to modify the selected student details.
5. Click **Delete** to remove a student from the database.
6. Click **Clear** to reset input fields.




## Author
**Nitin Singh**

