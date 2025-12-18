STUDENTS_CSV = "student.csv"
STUDENTS_TXT = "student.txt"


def get_last_id():
    """Get the last student ID from CSV file."""
    try:
        with open(STUDENTS_CSV, "r") as file:
            lines = file.readlines()
            if not lines:
                return 0
            last_line = lines[-1].strip()
            last_id = int(last_line.split(",")[0])
            return last_id
    except FileNotFoundError:
        return 0


def save_student_file(name, department):
    """Save student info to TXT and CSV files."""
    new_id = get_last_id() + 1

    # Save to TXT
    with open(STUDENTS_TXT, "a") as txt_file:
        txt_file.write(f"ID: {new_id}, Name: {name}, Department: {department}\n")

    # Save to CSV
    with open(STUDENTS_CSV, "a") as csv_file:
        csv_file.write(f"{new_id},{name},{department}\n")

    print(f"Student saved to {STUDENTS_TXT} and {STUDENTS_CSV} with ID {new_id}!")


def list_students():
    """Print all registered students from CSV file."""
    try:
        with open(STUDENTS_CSV, "r") as csv_file:
            lines = csv_file.readlines()
            if not lines:
                print("No students registered yet.")
                return

            print("\n--- REGISTERED STUDENTS ---")
            for line in lines:
                parts = line.strip().split(",")
                print(f"ID: {parts[0]} | Name: {parts[1]} | Department: {parts[2]}")
    except FileNotFoundError:
        print("No students registered yet.")


def register_student():
    """Register a new student and save."""
    name = input("Enter student's name: ").strip()
    department = input("Enter department: ").strip()
    save_student_file(name, department)


# Example usage
if __name__ == "__main__":
    register_student()  # Save a new student
    list_students()     # Display all students
