
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from results.resultservice import get_results_by_student
from courses.courseservice import load_courses
from students.studentservice import load_students


def calculate_gpa():
    """Generate grade report and calculate GPA for a student."""

    student_id = input("Enter student ID: ")

    # Load students
    students = load_students()
    student = next((s for s in students if str(s["id"]) == str(student_id)), None)

    if not student:
        print("Student not found!")
        return

    print(f"\n--- GRADE REPORT FOR {student['name'].upper()} ---")

    # Load courses and results
    courses = load_courses()
    results = get_results_by_student(student_id)

    if not results:
        print("No results found for this student.")
        return

    total_quality_points = 0
    total_units = 0

    print("\nCourse Results:")
    print("---------------------------------------------------------")
    print("Course Code | Course Title               | Units | Grade")
    print("---------------------------------------------------------")

    for r in results:
        course = next((c for c in courses if str(c["id"]) == str(r["course_id"])), None)

        if not course:
            print(f"Course ID {r['course_id']} not found! Skipping...")
            continue

        grade_point = grade_to_point(r["grade"])
        total_quality_points += grade_point * int(course["units"])
        total_units += int(course["units"])

        print(f"{course['code']:12} | {course['title'][:25]:25} | {course['units']:5} | {r['grade']}")

    if total_units == 0:
        print("\nNo valid course units found. Cannot calculate GPA.")
        return

    gpa = total_quality_points / total_units

    print("---------------------------------------------------------")
    print(f"Total Units: {total_units}")
    print(f"GPA: {gpa:.2f}")
    print("---------------------------------------------------------")


def grade_to_point(grade):
    """Convert a letter grade to GPA points."""
    grade = grade.upper()
    points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
    return points.get(grade, 0)


if __name__ == "__main__":
    calculate_gpa()

