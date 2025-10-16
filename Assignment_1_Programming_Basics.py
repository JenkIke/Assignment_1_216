"""
Isaac Jenkins, Jonathan Wall, and John Acilo
CPRG216-I Assignment 1
Oct 17, 2025
This is a grade registry program
Inputs: Student names and grades
Processing: Calculates the overall GPA for each student given the course grades
Outputs: Cumulative GPA for each student
"""

# Used to check if the program should continue running
running = True
# Initialize the dictionary to store student grades
grades_dict = {}

print("Welcome to the Grade Registry Program")

while running:
    # Set necessary variables to their starting values
    invalid_input = True
    student_grades = []
    subject_grade = 0
    # Will continue asking for input until a valid yes or no is given
    while invalid_input:
        new_student = input("Would you like to add a new student? y(yes), n(no)\n> ").lower()
        if new_student == "y" or new_student == "yes":
            adding_students = True
            invalid_input = False
        elif new_student == "n" or new_student == "no":
            adding_students = False
            invalid_input = False
        # If the given options aren't chosen, keep the loop going
        else:
            print("Incorrect Input, please enter y(yes),n(no)")

    # Will execute if y/yes was chosen
    if adding_students:
        student_name = input("Enter the student's name:\n> ").title()
        print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
        # Continue adding grades until -1 is the input
        while subject_grade != -1: 
            subject_grade = float(input("> ")) 
            # Subject grades must be between 0 and 4 to be valid
            if 0 <= subject_grade <= 4:
                student_grades.append(subject_grade)
            # Anything else that isnt -1 is invalid.
            elif subject_grade != -1:
                print("This is not a valid input. GPA must be between 0 and 4. Enter -1 to stop entering GPA")
        # Done adding grades so calculate gpa
        # Added logic for dividing by 0
        if len(student_grades) == 0:
            grades_dict[student_name] = 0
        else:
            grades_dict[student_name] = sum(student_grades) / len(student_grades)
        # Store gpa in dictionary paired with the students name
    # Will execute when n/no is chosen. The user is done adding students so print the gpa list
    else:
        if len(grades_dict) == 0:
            print("You have added no students. Thank you for using our application.")
            running = False
        else:
            # Print the results. Print the name in title case and format the GPA to 2 digits after the decimal
            print("This is the list of students in the system, and their corresponding accumulative GPA")
            for name in grades_dict:
                print(f"{name.title()} {grades_dict[name]:.2f}")
            running = False