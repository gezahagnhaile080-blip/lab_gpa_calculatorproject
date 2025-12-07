import json
import os

COURSES_FILE = "courses.json"


def load_courses():
    """Load courses from JSON file."""
    if not os.path.exists(COURSES_FILE):
        return []

    with open(COURSES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_courses(courses):
    """Save courses list back to JSON file."""
    with open(COURSES_FILE, "w") as f:
        json.dump(courses, f, indent=4)


def list_courses():
    """Print all registered courses."""
    courses = load_courses()

    if not courses:
        print("No courses registered yet.")
        return

    print("\n--- REGISTERED COURSES ---")
    for c in courses:
        print(f"ID: {c['id']} | Code: {c['code']} | Title: {c['title']} | Units: {c['units']}")


def register_course():
    """Register a new course and save it."""
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    units = input("Enter course units: ")

    try:
        units = int(units)
    except ValueError:
        print("Units must be a number!")
        return

    courses = load_courses()

    if courses:
        new_id = courses[-1]["id"] + 1
    else:
        new_id = 1

    new_course = {
        "id": new_id,
        "code": code,
        "title": title,
        "units": units
    }

    courses.append(new_course)
    save_courses(courses)

    print(f"Course '{title}' registered successfully with ID {new_id}!")
