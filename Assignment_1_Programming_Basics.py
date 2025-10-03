"""
CPRG216 Assignment 1
Isaac Jenkins, Jonathan Wall, and John Acilo
"""

"""
TODO:
ADD different output if the dictionary is empty?
ADD error handling if the first grade entered is -1 (Set student_gpa to 0 for that student)
Improve comments?
Make sure nothing is used past unit 2
"""

# Used to check if the program should continue running
running = True
# Initialize the dictionary to store student grades
grades_dict = {}


while running:
    # Set necessary variables to their starting values
    invalid_input = True
    total_grade = 0
    student_subjects = 0
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
                total_grade += subject_grade
                student_subjects += 1
            # Anything else that isnt -1 is invalid.
            elif subject_grade != -1:
                print("This is not a valid input. GPA must be between 0 and 4. Enter -1 to stop entering GPA")
        # Done adding grades so calculate gpa
        # Added logic for dividing by 0
        if student_subjects == 0:
            student_gpa = 0
        else:
            student_gpa = total_grade / student_subjects
        # Store gpa in dictionary paired with the students name
        grades_dict[student_name] = student_gpa
    # Will execute when n/no is chosen. The user is done adding students so print the gpa list
    else:
        for name in grades_dict:
            print(name, grades_dict[name])
        running = False