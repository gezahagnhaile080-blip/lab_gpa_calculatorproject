RESULTS_CSV = "result.csv"
RESULTS_TXT = "result.txt"


def calculate_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 85:
        return "A"
    elif score >= 80:
        return "A-"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "B-"
    elif score >= 60:
        return "C+"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "C-"
    elif score >= 40:
        return "D"
    else:
        return "F"


def register_result(student_id):
    """
    This function matches the app.py call:
    register_result(student_id)
    It asks for course and score, calculates grade,
    and saves results to CSV and TXT files.
    """
    course_id = input("Enter course ID: ").strip()
    score_input = input("Enter score (0–100): ").strip()

    try:
        score = float(score_input)
        if not (0 <= score <= 100):
            print("Score must be between 0 and 100!")
            return
    except ValueError:
        print("Invalid score!")
        return

    grade = calculate_grade(score)

    # Save to CSV
    with open(RESULTS_CSV, "a") as csv_file:
        csv_file.write(f"{student_id},{course_id},{score},{grade}\n")

    # Save to TXT
    with open(RESULTS_TXT, "a") as txt_file:
        txt_file.write(f"Student ID: {student_id}, Course ID: {course_id}, Score: {score}, Grade: {grade}\n")

    print(f"Result saved: Student {student_id} | Course {course_id} | Score {score} | Grade {grade}")


def get_results_by_student(student_id):
    """Return a list of results for the given student from CSV."""
    results = []
    try:
        with open(RESULTS_CSV, "r") as csv_file:
            for line in csv_file:
                parts = line.strip().split(",")
                if len(parts) == 4 and parts[0] == str(student_id):
                    results.append({
                        "student_id": parts[0],
                        "course_id": parts[1],
                        "score": float(parts[2]),
                        "grade": parts[3]
                    })
    except FileNotFoundError:
        pass  # File not created yet
    return results
