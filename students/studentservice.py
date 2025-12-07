import json
import os

STUDENTS_FILE = "students.json"


def load_students():
    """Load students from JSON file, return list."""
    if not os.path.exists(STUDENTS_FILE):
        return []

    with open(STUDENTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_students(students):
    """Save students list back to JSON file."""
    with open(STUDENTS_FILE, "w") as f:
        json.dump(students, f, indent=4)


def list_students():
    """Print all registered students."""
    students = load_students()

    if not students:
        print("No students registered yet.")
        return

    print("\n--- REGISTERED STUDENTS ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Department: {s['department']}")


def register_student():
    """Register a new student and save."""
    name = input("Enter student's name: ")
    department = input("Enter department: ")

    students = load_students()

    if students:
        new_id = students[-1]["id"] + 1
    else:
        new_id = 1

    new_student = {
        "id": new_id,
        "name": name,
        "department": department
    }

    students.append(new_student)
    save_students(students)

    print(f"Student '{name}' registered successfully with ID {new_id}!")
