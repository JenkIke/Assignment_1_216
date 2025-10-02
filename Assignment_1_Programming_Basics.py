running = True
grades_dict = {}

"""
TODO:
Add error handling if gpa isnt between 0 and 4
Add comments
Add different output if the dictionary is empty?
"""


while running:
    invalid_input = True
    total_grade = 0
    student_subjects = 0
    subject_grade = 0
    while invalid_input:
        new_student = input("Would you like to add a new student? y(yes), n(no)\n> ").lower()
        if new_student == "y" or new_student == "yes":
            adding_students = True
            invalid_input = False
        elif new_student == "n" or new_student == "no":
            adding_students = False
            invalid_input = False
        else:
            print("Incorrect Input, please enter y(yes),n(no)")
            invalid_input = True

    if adding_students:
        student_name = input("Enter the student's name:\n> ").title()
        while subject_grade != -1: 
            subject_grade = float(input("Enter student GPA for each subject. Enter -1 to stop entering GPA.\n> "))
            if subject_grade != -1:
                total_grade += subject_grade
                student_subjects += 1
        student_gpa = total_grade / student_subjects
        grades_dict[student_name] = student_gpa
    else:
        for name in grades_dict:
            print(name, grades_dict[name])
        running = False