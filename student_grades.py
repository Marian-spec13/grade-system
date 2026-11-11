"""
Program: Student Grade Management System
Author: Marian
Framework: Personal Software Process (PSP)
Description: Accepts student marks, validates inputs, calculates averages, and outputs letter grades.
"""

def get_valid_mark(subject_name):
    """Prompt user for a valid numerical mark between 0 and 100 with error handling."""
    while True:
        try:
            mark = float(input(f"Enter mark for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("❌ Error: Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a numerical value.")

def calculate_letter_grade(average):
    """Determine letter grade based on standard grading thresholds."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=" * 45)
    print("      STUDENT GRADE MANAGEMENT SYSTEM (PSP)")
    print("=" * 45)
    
    # Input student details
    student_name = input("Enter student's full name: ").strip()
    
    subjects = ["Mathematics", "English", "Science"]
    marks = []
    
    # Capture marks with validation
    for subj in subjects:
        mark = get_valid_mark(subj)
        marks.append(mark)
    
    # Calculations
    total_marks = sum(marks)
    average_mark = total_marks / len(subjects)
    letter_grade = calculate_letter_grade(average_mark)
    
    # Display Results / Report Card
    print("\n" + "=" * 45)
    print(f"REPORT CARD FOR: {student_name.upper()}")
    print("=" * 45)
    for i in range(len(subjects)):
        print(f" • {subjects[i]:<12}: {marks[i]:.2f}")
    print("-" * 45)
    print(f" Total Marks    : {total_marks:.2f}")
    print(f" Average Mark   : {average_mark:.2f}")
    print(f" Letter Grade   : {letter_grade}")
    print("=" * 45)

if __name__ == "__main__":
    main()