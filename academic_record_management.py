"""
Academic Record Management System
A simple CLI application to manage student records using a dictionary.
"""

# Global dictionary to store student data
student = {}


def add_student():
    """Add a new student record."""
    print("\n--- Add Student ---")
    reg = input("Enter Registration Number: ").strip()

    if reg in student:
        print("Student with this Registration Number already exists!")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    course = input("Enter Course: ").strip()
    if not course:
        print("Course cannot be empty!")
        return

    cgpa = input("Enter CGPA: ").strip()

    # Validate CGPA
    try:
        cgpa = float(cgpa)
        if not (0 <= cgpa <= 10):
            print("CGPA must be between 0 and 10.")
            return
    except ValueError:
        print("Invalid CGPA! Please enter a number.")
        return

    state = input("Enter State: ").strip()
    if not state:
        print("State cannot be empty!")
        return

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

    if reg in student:
        info = student[reg]
        print("\nRecord Found:")
        print(f"Registration Number : {reg}")
        print(f"Name               : {info['name']}")
        print(f"Course             : {info['course']}")
        print(f"CGPA               : {info['cgpa']}")
        print(f"State              : {info['state']}")
    else:
        print("Student not found!")


def update_student():
    """Update an existing student record."""
    print("\n--- Update Student ---")
    reg = input("Enter Registration Number: ").strip()

    if reg not in student:
        print("Student not found!")
        return

    current = student[reg]
    print("Leave field blank to keep current value.")

    name = input(f"Name ({current['name']}): ").strip()
    course = input(f"Course ({current['course']}): ").strip()
    cgpa = input(f"CGPA ({current['cgpa']}): ").strip()
    state = input(f"State ({current['state']}): ").strip()

    if name:
        current["name"] = name
    if course:
        current["course"] = course
    if cgpa:
        try:
            cgpa = float(cgpa)
            if 0 <= cgpa <= 10:
                current["cgpa"] = cgpa
            else:
                print("CGPA must be between 0 and 10. Keeping old value.")
        except ValueError:
            print("Invalid CGPA! Keeping old value.")
    if state:
        current["state"] = state

    print("Record updated successfully!")


def delete_student():
    """Delete a student record."""
    print("\n--- Delete Student ---")
    reg = input("Enter Registration Number: ").strip()

    if reg in student:
        confirm = input("Are you sure you want to delete? (y/n): ").lower()
        if confirm == 'y':
            del student[reg]
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found!")


def display_all():
    """Display all student records."""
    print("\n--- All Student Records ---")
    if not student:
        print("No records found.")
        return

    print("-" * 60)
    print(f"{'Reg No':<12} {'Name':<15} {'Course':<15} {'CGPA':<6} {'State':<10}")
    print("-" * 60)

    # Sorted display
    for reg in sorted(student):
        info = student[reg]
        print(f"{reg:<12} {info['name']:<15} {info['course']:<15} "
              f"{info['cgpa']:<6} {info['state']:<10}")

    print("-" * 60)


def main():
    """Main menu loop."""
    while True:
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

        try:
            choice = input("Enter your choice (1-6): ").strip()
        except Exception:
            print("Invalid input!")
            continue

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


if __name__ == "__main__":
    main()
