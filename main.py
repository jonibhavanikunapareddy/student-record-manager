# Import the json module.
# Used to read and write student data in JSON format.
import json

# Import the re module.
# Used to validate the email address.
import re

# Import datetime.
# Used to record the date and time of errors.
from datetime import datetime


# Name of the file used to store student records.
STUDENT_FILE = "students.json"

# Name of the file used to store error messages.
ERROR_FILE = "error_log.txt"


# ---------------------------------------------------------
# FUNCTION: read_students()
# PURPOSE: Read student records from students.json
# ---------------------------------------------------------

def read_students():

    # Try to open and read the JSON file.
    try:

        # Open students.json in read mode.
        with open(STUDENT_FILE, "r") as file:

            # Convert JSON data into Python data.
            return json.load(file)

    # If students.json does not exist.
    except FileNotFoundError:

        # Return an empty list.
        return []

    # If students.json is empty or contains invalid JSON.
    except json.JSONDecodeError:

        # Return an empty list instead of crashing.
        return []


# ---------------------------------------------------------
# FUNCTION: save_students()
# PURPOSE: Save student records into students.json
# ---------------------------------------------------------

def save_students(students):

    # Open students.json in write mode.
    # If the file does not exist, it will be created.
    with open(STUDENT_FILE, "w") as file:

        # Convert Python data into JSON.
        # indent=4 makes the JSON easier to read.
        json.dump(students, file, indent=4)


# ---------------------------------------------------------
# FUNCTION: log_error()
# PURPOSE: Save errors with student name and time
# ---------------------------------------------------------

def log_error(error, student_name="Unknown"):

    # Get the current date and time.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open error_log.txt in append mode.
    # "a" means old errors will not be deleted.
    with open(ERROR_FILE, "a") as file:

        # Write time, student name and error message.
        file.write(
            f"[{current_time}] Student: {student_name} | Error: {error}\n"
        )


# ---------------------------------------------------------
# FUNCTION: validate_email()
# PURPOSE: Check whether the email has a valid format
# ---------------------------------------------------------

def validate_email(email):

    # Regular expression pattern for a basic email format.
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Check whether the email matches the pattern.
    if not re.match(pattern, email):

        # Create an error if the email is invalid.
        raise ValueError("Invalid email address.")

    # Return True if the email is valid.
    return True


# ---------------------------------------------------------
# FUNCTION: add_student()
# PURPOSE: Add a new student
# ---------------------------------------------------------

def add_student():

    # Set a default name.
    # This is useful if an error occurs before the name is entered.
    name = "Unknown"

    # Start error handling.
    try:

        # Read existing student records.
        students = read_students()

        # Ask the user for Student ID.
        student_id = input("Enter Student ID: ").strip()

        # Ask the user for Student Name.
        name = input("Enter Student Name: ").strip()

        # Ask the user for Student Email.
        email = input("Enter Student Email: ").strip()

        # Ask the user for Course.
        course = input("Enter Course: ").strip()


        # Check whether Student ID is empty.
        if not student_id:

            # Generate an error.
            raise ValueError("Student ID cannot be empty.")


        # Check whether student name is empty.
        if not name:

            # Generate an error.
            raise ValueError("Student name cannot be empty.")


        # Check whether course is empty.
        if not course:

            # Generate an error.
            raise ValueError("Course cannot be empty.")


        # Check every existing student.
        for student in students:

            # Check whether the entered ID already exists.
            if student["id"] == student_id:

                # Generate duplicate ID error.
                raise ValueError("Duplicate Student ID.")


        # Validate the email address.
        validate_email(email)


        # Create a dictionary for the new student.
        new_student = {
            "id": student_id,
            "name": name,
            "email": email,
            "course": course
        }


        # Add the new student to the list.
        students.append(new_student)


        # Save the updated list.
        save_students(students)


        # Display success message.
        print("Student added successfully.")


    # Catch ValueError errors.
    except ValueError as error:

        # Save the error with the student's name.
        log_error(error, name)

        # Display the error.
        print(f"Error: {error}")


# ---------------------------------------------------------
# FUNCTION: display_students()
# PURPOSE: Display all student records
# ---------------------------------------------------------

def display_students():

    # Read all students.
    students = read_students()


    # Check whether the list is empty.
    if not students:

        # Display message if there are no records.
        print("No student records found.")

        # Stop the function.
        return


    # Display heading.
    print("\nStudent Records")

    # Display a separator.
    print("-" * 40)


    # Loop through all students.
    for student in students:

        # Display Student ID.
        print(f"ID     : {student['id']}")

        # Display Student Name.
        print(f"Name   : {student['name']}")

        # Display Student Email.
        print(f"Email  : {student['email']}")

        # Display Student Course.
        print(f"Course : {student['course']}")

        # Display separator.
        print("-" * 40)


# ---------------------------------------------------------
# FUNCTION: search_student()
# PURPOSE: Search for a student using Student ID
# ---------------------------------------------------------

def search_student():

    # Set a default value for the ID.
    student_id = "Unknown"

    # Start error handling.
    try:

        # Read all students.
        students = read_students()

        # Ask the user for Student ID.
        student_id = input("Enter Student ID to search: ").strip()


        # Search through all students.
        for student in students:

            # Compare entered ID with stored ID.
            if student["id"] == student_id:

                # Display heading.
                print("\nStudent Found")

                # Display Student ID.
                print(f"ID     : {student['id']}")

                # Display Student Name.
                print(f"Name   : {student['name']}")

                # Display Student Email.
                print(f"Email  : {student['email']}")

                # Display Student Course.
                print(f"Course : {student['course']}")

                # Stop searching.
                return


        # If no student was found.
        raise ValueError("Student ID not found.")


    # Catch the ValueError.
    except ValueError as error:

        # Log the searched ID with the error.
        log_error(error, f"ID {student_id}")

        # Display the error.
        print(f"Error: {error}")


# ---------------------------------------------------------
# FUNCTION: main()
# PURPOSE: Display menu and control the program
# ---------------------------------------------------------

def main():

    # Continue displaying the menu until the user exits.
    while True:

        # Display program title.
        print("\n===== Student Record Manager =====")

        # Display option 1.
        print("1. Add Student")

        # Display option 2.
        print("2. View All Students")

        # Display option 3.
        print("3. Search Student")

        # Display option 4.
        print("4. Exit")


        # Ask the user for a menu choice.
        choice = input("Enter your choice: ").strip()


        # If the user chooses option 1.
        if choice == "1":

            # Call add_student().
            add_student()


        # If the user chooses option 2.
        elif choice == "2":

            # Call display_students().
            display_students()


        # If the user chooses option 3.
        elif choice == "3":

            # Call search_student().
            search_student()


        # If the user chooses option 4.
        elif choice == "4":

            # Display goodbye message.
            print("Thank you for using Student Record Manager.")

            # Exit the while loop.
            break


        # If the user enters an invalid choice.
        else:

            # Create an error.
            error = ValueError("Invalid menu choice.")

            # Log the error.
            log_error(error, "Unknown")

            # Display an error message.
            print("Error: Please enter a number from 1 to 4.")


# ---------------------------------------------------------
# PROGRAM STARTING POINT
# ---------------------------------------------------------

# Check whether this Python file is being run directly.
if __name__ == "__main__":

    # Start the program.
    main()
