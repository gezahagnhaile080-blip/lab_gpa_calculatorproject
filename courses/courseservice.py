COURSES_CSV = "course.csv"
COURSES_TXT = "course.txt"


def get_last_course_id():
    """Get the last numeric course ID from CSV file."""
    try:
        with open(COURSES_CSV, "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                first_col = line.strip().split(",")[0]
                if first_col.isdigit():
                    return int(first_col)
            return 0
    except FileNotFoundError:
        return 0


def save_course_file(course_id, code, title, credits):
    """Save course info to TXT and CSV files."""
    # Save to TXT
    with open(COURSES_TXT, "a") as txt_file:
        txt_file.write(f"ID: {course_id} | Code: {code:12} | Title: {title:25} | Units: {credits}\n")

    # Save to CSV
    with open(COURSES_CSV, "a") as csv_file:
        csv_file.write(f"{course_id},{code},{title},{credits}\n")

    print(f"Course '{title}' saved with ID {course_id}!")


def register_course():
    """Register a new course (prompt user for input)."""
    code = input("Enter course code: ").strip()
    title = input("Enter course title: ").strip()
    credits = input("Enter course credits: ").strip()
    numeric_id = get_last_course_id() + 1
    save_course_file(numeric_id, code, title, credits)


def list_courses():
    """List all registered courses."""
    try:
        with open(COURSES_CSV, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No courses registered yet.")
                return
            print("\n--- COURSES ---")
            for line in lines:
                parts = line.strip().split(",")
                print(f"ID: {parts[0]} | Code: {parts[1]} | Title: {parts[2]} | Units: {parts[3]}")
    except FileNotFoundError:
        print("No courses registered yet.")
