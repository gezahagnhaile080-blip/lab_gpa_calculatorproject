import json
import os

COURSES_FILE = "courses.json"

def load_courses():
    if not os.path.exists(COURSES_FILE):
        return []
    with open(COURSES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_courses(courses):
    with open(COURSES_FILE, "w") as f:
        json.dump(courses, f, indent=4)

def register_course():
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    units = input("Enter course units: ")
    courses = load_courses()
    new_id = courses[-1]["id"] + 1 if courses else 1
    courses.append({"id": new_id, "code": code, "title": title, "units": units})
    save_courses(courses)
    print(f"Course '{title}' registered with ID {new_id}")

def save():
    code = input("Course code: ")
    title = input("Course title: ")
    units = input("Course units: ")
    with open("course.txt", "a") as txt, open("course.csv", "a") as csv:
        txt.write(f"{code:12} | {title:25} | {units}\n")
        csv.write(f"{code},{title},{units}\n")
    print(f"Saved: {code}, {title}, {units}")

def list_courses():
    courses = load_courses()
    if not courses:
        print("No courses registered yet.")
        return
    print("\n--- COURSES ---")
    for c in courses:
        print(f"ID: {c['id']} | Code: {c['code']} | Title: {c['title']} | Units: {c['units']}")

if __name__ == "__main__":
    while True:
        action = input("\nEnter 'r' to register, 's' to save manually, 'l' to list, 'q' to quit: ").lower()
        if action == "r":
            register_course()
        elif action == "s":
            save()
        elif action == "l":
            list_courses()
        elif action == "q":
            print("Exiting.")
            break
        else:
            print("Invalid input.")
