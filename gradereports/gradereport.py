import csv
from results.resultservice import get_results_by_student

STUDENTS_CSV = "student.csv"
COURSES_CSV = "course.csv"
GRADEREPORT_CSV = "gradereport.csv"
GRADEREPORT_TXT = "gradereport.txt"

def load_students():
    """Load students from CSV file."""
    students = []
    try:
        with open(STUDENTS_CSV, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    students.append({"id": parts[0], "name": parts[1]})
    except FileNotFoundError:
        pass
    return students

def load_courses():
    """Load courses from CSV file."""
    courses = []
    try:
        with open(COURSES_CSV, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 4:
                    courses.append({
                        "id": parts[0],
                        "code": parts[1],
                        "title": parts[2],
                        "units": parts[3]
                    })
    except FileNotFoundError:
        pass
    return courses

def grade_to_point(grade):
    """Convert letter grade to GPA points."""
    grade = grade.upper()
    points = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7,
              "C+": 2.3, "C": 2, "C-": 1.7, "D": 1, "F": 0}
    return points.get(grade, 0)

def calculate_gpa():
    """Generate grade report and calculate GPA for a student."""
    student_id = input("Enter student ID: ").strip()
    students = load_students()

    student = next((s for s in students if str(s["id"]) == str(student_id)), None)
    if not student:
        print("Student not found!")
        return

    print(f"\n--- GRADE REPORT FOR {student['name'].upper()} ---")

    courses = load_courses()
    results = get_results_by_student(student_id)

    if not results:
        print("No results found for this student.")
        return

    total_grade_points = 0
    total_credits = 0

    print("\nCourse Results:")
    print("---------------------------------------------------------")
    print(f"{'Course Code':12} | {'Course Title':25} | {'Credits':7} | {'Grade'}")
    print("---------------------------------------------------------")

    with open(GRADEREPORT_CSV, "w") as csv_file, open(GRADEREPORT_TXT, "w") as txt_file:
        csv_file.write("Course Code,Course Title,Credits,Grade\n")
        txt_file.write(f"{'Course Code':12} | {'Course Title':25} | {'Credits':7} | {'Grade'}\n")
        txt_file.write("---------------------------------------------------------\n")

        for r in results:
            course = next((c for c in courses if str(c["id"]) == str(r["course_id"])), None)
            if not course:
                print(f"Course ID {r['course_id']} not found! Skipping...")
                continue

            try:
                credits = float(course.get("units", 0))
            except (ValueError, TypeError):
                print(f"Invalid credits for course {course['code']}. Skipping...")
                continue

            grade_point = grade_to_point(r.get("grade", "F"))
            total_grade_points += grade_point * credits
            total_credits += credits

            # Print and save to files
            line_txt = f"{course['code']:12} | {course['title'][:25]:25} | {credits:7} | {r['grade']}"
            print(line_txt)
            txt_file.write(line_txt + "\n")
            csv_file.write(f"{course['code']},{course['title']},{credits},{r['grade']}\n")

    if total_credits == 0:
        print("\nNo valid course credits found. Cannot calculate GPA.")
        return

    gpa = total_grade_points / total_credits
    print("---------------------------------------------------------")
    print(f"Total Credits: {total_credits}")
    print(f"GPA: {gpa:.2f}")
    print("---------------------------------------------------------")
    print(f"\nGrade report saved to {GRADEREPORT_CSV} and {GRADEREPORT_TXT}")
