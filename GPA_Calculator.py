
grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

# Function to calculate GPA
def calculate_gpa():
    total_credit_hours = 0
    total_grade_points = 0.0

    try:
        num_subjects = int(input("Enter the number of subjects: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i in range(num_subjects):
        print(f"\nSubject {i + 1}:")

        grade = input("Enter the grade (e.g., A, B+, C): ").strip().upper()

        if grade not in grade_points:
            print("Invalid grade entered. Please enter a valid grade (A, B+, C, etc.).")
            return

        try:
            credit_hours = float(input("Enter the credit hours for this subject: "))  # Prompt for credit hours
            if credit_hours <= 0:
                print("Credit hours must be a positive number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number for credit hours.")
            return

        # Calculate total grade points
        points = grade_points[grade] * credit_hours
        total_grade_points += points
        total_credit_hours += credit_hours

    # Calculate GPA
    if total_credit_hours > 0:
        gpa = total_grade_points / total_credit_hours
        print(f"\nTotal Credit Hours: {total_credit_hours}")
        print(f"Total Grade Points: {total_grade_points:.2f}")
        print(f"Calculated GPA: {gpa:.2f}")
    else:
        print("No credit hours entered. GPA cannot be calculated.")


if __name__ == "__main__":
    calculate_gpa()