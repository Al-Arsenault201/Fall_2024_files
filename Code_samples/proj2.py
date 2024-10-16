# a database manipulation problem similar to what will
# be covered in project 2

# each student record is contained in a dictionary
# a section is a list of student records

section = []  # we start with an empty list
n_students = int(input("How many students are in this section? "))
for i in range(n_students):
    student = {}  # start with an empty dictionary
    name = input("Student Name: ")
    id = input("Student ID: ")
    test_grades = []
    project_grades = []
    for j in range(3):
        t = int(input("Enter the next test grade"))
        p = int(input("Enter the next project grade"))
        test_grades.append(t)
        project_grades.append(p)

    # now we have to load all the data into the student
    # record. Fortunately, we know how to add things to a dictionary
    student["Name"] = name
    student["ID"] = id
    student["Test Grades"] = test_grades
    student["Project Grades"] = project_grades
    section.append(student)
    print("Section so far: ", section)

