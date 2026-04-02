"""
Academic Record Management System
A simple CLI application to manage student records using a dictionary.
"""

# Global dictionary to store student data
# Key: registration number (string)
# Value: another dictionary with keys: name, course, cgpa, state
student = {}


def add_student():
    """Add a new student record."""
    print("\n--- Add Student ---")
    reg = input("Enter Registration Number: ").strip()

    # Check if registration number already exists
    if reg in student:
        print("Student with this Registration Number already exists!")
        return

    # Collect student details
    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    cgpa = input("Enter CGPA: ").strip()

    # Validate CGPA: ensure it can be converted to a float (number)
    try:
        float(cgpa)  # This will raise ValueError if not a number
    except ValueError:
        print("Invalid CGPA! Please enter a number. Record not added.")
        return

    state = input("Enter State: ").strip()

    # Store the record: registration number maps to a dictionary of details
    student[reg] = {
        "name": name,
        "course": course,
        "cgpa": cgpa,
        "state": state
    }
    print("Student added successfully!")


def search_student():
    """Search and display a student by registration number."""
    print("\n--- Search Student ---")
    reg = input("Enter Registration Number: ").strip()

    # Check if the registration number exists in the dictionary
    if reg in student:
        info = student[reg]  # Retrieve the student's details
        print("\nRecord Found:")
        print(f"Registration Number : {reg}")
        print(f"Name               : {info['name']}")
        print(f"Course             : {info['course']}")
        print(f"CGPA               : {info['cgpa']}")
        print(f"State              : {info['state']}")
    else:
        print("Student not found!")


def update_student():
    """Update an existing student record. Leave field empty to keep current value."""
    print("\n--- Update Student ---")
    reg = input("Enter Registration Number: ").strip()

    # Exit if student does not exist
    if reg not in student:
        print("Student not found!")
        return

    current = student[reg]  # Get the existing data
    print("Leave field blank to keep current value.")

    # For each field, ask for new value. If input is empty, keep the old one.
    name = input(f"Name ({current['name']}): ").strip()
    course = input(f"Course ({current['course']}): ").strip()
    cgpa = input(f"CGPA ({current['cgpa']}): ").strip()
    state = input(f"State ({current['state']}): ").strip()

    # Update only if user provided a non‑empty value
    if name:
        current["name"] = name
    if course:
        current["course"] = course
    if cgpa:
        # Validate the new CGPA before updating
        try:
            float(cgpa)
            current["cgpa"] = cgpa
        except ValueError:
            print("Invalid CGPA! Keeping old value.")
    if state:
        current["state"] = state

    print("Record updated successfully!")


def delete_student():
    """Delete a student record."""
    print("\n--- Delete Student ---")
    reg = input("Enter Registration Number: ").strip()

    # Use 'del' to remove the key-value pair from the dictionary
    if reg in student:
        del student[reg]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def display_all():
    """Display all student records in a formatted table."""
    print("\n--- All Student Records ---")
    if not student:
        print("No records found.")
        return

    # Print a header with column names
    print("-" * 60)
    print(f"{'Reg No':<12} {'Name':<15} {'Course':<15} {'CGPA':<6} {'State':<10}")
    print("-" * 60)

    # Loop through all items in the student dictionary
    for reg, info in student.items():
        # Print each record in a row, using left‑aligned columns
        print(f"{reg:<12} {info['name']:<15} {info['course']:<15} "
              f"{info['cgpa']:<6} {info['state']:<10}")
    print("-" * 60)


def main():
    """Main menu loop – runs until user chooses Exit."""
    while True:
        # Display the menu
        print("\n" + "=" * 40)
        print("     STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        print("-" * 40)

        # Get user's choice as a string (to avoid crash on non‑integer input)
        choice = input("Enter your choice (1-6): ").strip()

        # Call the appropriate function based on choice
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("\nExiting program. Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# This ensures the program runs only when executed directly,
# not when imported as a module.
if __name__ == "__main__":
    main()
