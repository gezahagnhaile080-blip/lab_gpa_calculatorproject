from students.studentservice import register_student, list_students
from courses.courseservice import register_course, list_courses
from results.resultservice import register_result
from gradereports.gradereport import calculate_gpa

def main_menu():
    while True:
        print("\n==== GPA CALCULATOR ====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Reports")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n--- STUDENTS ---")
            list_students()
            add_more = input("Do you want to register a new student? (y/n): ").strip().lower()
            if add_more == "y":
                register_student()

        elif choice == "2":
            print("\n--- COURSES ---")
            list_courses()
            add_more = input("Do you want to register a new course? (y/n): ").strip().lower()
            if add_more == "y":
                register_course()

        elif choice == "3":
            print("\n--- RESULTS ---")
            sid = input("Enter student ID: ").strip()
            register_result(sid)

        elif choice == "4":
            print("\n--- GRADE REPORT ---")
            calculate_gpa()

        elif choice == "5":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main_menu()
