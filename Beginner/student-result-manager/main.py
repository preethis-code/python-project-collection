# -----------------------------------------
# Student Result Management System
# A simple CLI-based Python project
# -----------------------------------------

# Dictionary to store student data
students = {}

# Function to display menu
def display_menu():
    print("\n----- Student Result Manager -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")


# Function to add a student
def add_student():
    name = input("Enter student name: ").strip()

    try:
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} successfully added!")
    except ValueError:
        print("Invalid marks! Please enter a number.")


# Function to view all students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for name, marks in students.items():
            print(f"{name} : {marks}")


# Function to check result
def check_result():
    name = input("Enter student name: ").strip()

    if name in students:
        marks = students[name]

        if marks >= 40:
            print(f"{name} has successfully passed the exam!")
        else:
            print(f"{name} has failed the exam.")
    else:
        print("Student not found.")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        check_result()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid input! Please try again.")


