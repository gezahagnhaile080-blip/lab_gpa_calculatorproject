import json
import os

RESULTS_FILE = "results.json"


def load_results():
    """Load results from JSON file."""
    if not os.path.exists(RESULTS_FILE):
        return []

    with open(RESULTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_results(results):
    """Save results list back to JSON file."""
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)


def register_result(student_id):
    """Register a result for a student."""
    course_id = input("Enter course ID: ")
    score = input("Enter score (0–100): ")

    try:
        score = float(score)
        if score < 0 or score > 100:
            print("Score must be between 0 and 100!")
            return
    except ValueError:
        print("Invalid score!")
        return

    grade = calculate_grade(score)

    results = load_results()

    new_result = {
        "student_id": student_id,
        "course_id": course_id,
        "score": score,
        "grade": grade
    }

    results.append(new_result)
    save_results(results)

    print(f"Result recorded: Student {student_id} | Course {course_id} | Score {score} | Grade {grade}")


def calculate_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def get_results_by_student(student_id):
    """Return a list of results for the given student."""
    results = load_results()
    return [r for r in results if str(r["student_id"]) == str(student_id)]
