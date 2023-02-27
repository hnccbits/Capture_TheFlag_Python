# Student Management System Python

![ctf.jpeg](Images/ctf.jpeg)

## **Overview**

This project is a program for managing student records. It allows the user to create, view, search, update, and delete student records. The program uses an array of structures to store the student records.

## Rules :

1. Each team can participate in only one programming language.
2. To participate, you must fork this repository, make the necessary
changes to the file(s), and then create a pull request (PR) on the main
branch with the correct code.
3. Teams will be ranked based on the time they take to create the PR and the accuracy of their code.
4. For time-based ranking, only the time taken for the last commit will be considered. Multiple commits can be made in a single PR.
5. Any commit made after 12 pm will not be considered for any team.
6. To be ranked based on code, your submitted code must solve all the bugs listed in the project description.
7. You are allowed to explain your changes using comments.
8. We hope these rules are clear and easy to follow. Good luck with the contest!

## **Features**

The program starts by asking the user to enter the number of student records they want to create. The maximum number of records is 20, and if the user enters a number greater than 20, the program limits the number of records to 20.

The user is then presented with a menu that allows them to perform various operations on the student records. The menu has the following options:

1. Insert Record: Allows the user to add a new student record to the array.
2. Delete Record: Allows the user to delete a student record from the array by entering the student ID.
3. Search Record: Allows the user to search for a student record by entering the student ID.
4. Update Record: Allows the user to update a student record by entering the student ID.
5. Display Record: Displays all the student records stored in the array.
6. Exit: Exits the program.

The program uses a flag variable to indicate whether a student record with the given student ID was found or not.

## **Working Description**

This program allows an admin to manage a table of student data, with a maximum of 20 students that can be stored. The following functions are available for the admin to manage the student records:

1. **`Build()`**: This function helps in initializing student details, where the admin is first asked for the number of students to enter, and then the admin can enter the data of each student respectively.
2. **`Insert()`**: This function helps in inserting a new student detail into the current table.
3. **`DeleteRecord()`**: This works with the help of another function, which is **`DeleteIndex()`**. First, **`DeleteRecord()`** takes the input of the student ID from the admin and searches for the student in the record. If the student is found, then it passes the index of the student to **`DeleteIndex()`** function for deleting the student record.
4. **`SearchRecord()`**: This function searches for the details of a student in the record using the student ID taken as an input from the admin. If the student is found, then it displays the record of the student on the screen.
5. **`DisplayRecord()`**: This function helps in displaying the details of all students in the record.
6. **`UpdateRecord()`**: This function searches for a student in the record using the student ID taken as an input from the admin. If the student is found, then it updates the new details of the student that are input by the admin.
7. **`ShowMenu()`**: It displays all available options of the project for the admin. From here, the admin can navigate to all functions. This is one of the main functions of the project. When the user selects an option from the menu, the program calls a function that performs the selected operation. Each function performs the required operation on the array of structures.

## Installation

### **Prerequisites**

To run the above Python program on your local system, you would need to have Python installed. Here are the general steps to follow:

1. Download and install Python on your local machine. You can download the latest version of Python from the official Python website: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Open a text editor or an IDE (Integrated Development Environment) such as PyCharm, Visual Studio Code, or Spyder.

### Setup

1. Fork this repository
2. Clone the repository to your local computer 
3. Run in terminal
    - Navigate to the project directory and open terminal in project root
    - Run the command `python StudentManagement.py`  and press enter
    - The output of the program should be displayed on the console or terminal window.
4. Run in IDE
    - Open project directory in your IDE (e.g. VS Code or Pycharm)
    - Open `[StudentManagement.py](http://StudentManagement.py)` file and run this file

## Bugs

The following bugs are present in the program:

1. The program allows for duplicate student IDs to be stored, which means that different students could have the same ID. This needs to be fixed to ensure that each student has a unique ID.
2. The search function has a bug that incorrectly identifies and displays the student record that matches the entered student ID.
3. The update function is not correctly updating the student record with new details entered by the admin. This needs to be fixed.
4. The student records are not displayed in proper order when using the display function.
5. The program terminates when the display function finishes displaying the records, instead of returning to the main menu.
6. There is a bug in the delete function that is causing student records to not be deleted properly.

## Task

The task is to resolve all the identified bugs within the employee management system, and to create a pull request (PR) with the proposed fixes.
