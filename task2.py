

def input_grades():
    grades = {}
    print("Enter grades for different subjects or assignments. Type 'done' when finished.")
    
    while True:
        subject = input("Enter subject or assignment name: ")
        if subject.lower() == 'done':
            break
        grade = input(f"Enter grade for {subject}: ")
        try:
            grades[subject] = float(grade)
        except ValueError:
            print("Invalid grade. Please enter a number.")
    
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    total = sum(grades.values())
    count = len(grades)
    return total / count

def get_letter_grade(average):
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

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def display_results(grades, average, letter_grade, gpa):
    print("\nGrades Summary:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

def main():
    grades = input_grades()
    if not grades:
        print("No grades entered.")
        return

    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    gpa = calculate_gpa(average)

    display_results(grades, average, letter_grade, gpa)

main()
