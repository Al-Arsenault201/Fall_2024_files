from matplotlib import pyplot as plt


FILES = ["Fall_2025.csv","Fall_2026.csv","Spring_2026.csv"]
GRADES = ["A", "B", "C", "D", "F"]

def convert_student_to_dict(student):#student is the student record as a list
    s = {}
    s["last_name"] = student[0]
    s["first_name"] = student[1]
    s["student_id"] = student[2]
    s["P1"] = student[3]
    s["P2"] = student[4]
    s["P3"] = student[5]
    s["T1"] = student[6]
    s["T2"] = student[7]
    s["T3"] = student[8]

    return s

def read_file(fname):
    with open(fname, "r") as infile:
        infile.readline()
        infile.readline()
        students = infile.readlines()
 #       print(students)
        for i in range(len(students)):
            students[i] = students[i].split(",")
 #       print(students)
            students[i][0] = students[i][0].replace('"','')
            students[i][1] = students[i][1].replace('"','')
 #           print(students[i])
            students[i] = convert_student_to_dict(students[i])
        return students

def get_semester():
    VALIDS = ["F","f","S","s","T","t","U", "u"]
    print("\n \n\n\n\n")
    print("In which semester was the student enrolled?\n")
    print("Enter F for Fall 2025\n")
    print("Enter S for Spring 2026\n")
    print("Enter T for Fall 2026\n")
    print("Enter U if you do not know\n")
    answer = input("Enter your semester: ")
    while answer not in VALIDS:
        print("That is an error; please try again.")
        answer = input("Enter your semester: ")
    return answer.upper()

def search_by_student_id(database, ID):
    when = get_semester()
    if when == "F":
        found = False
        for i in range(len(database[0])):
            if database[0][i]['Student ID'] == ID:
                found = True
                print(database[0][i]['Final_grade'])
    elif when == "S":
        found = False
        for i in range(len(database[1])):
            if database[1][i]['Student ID'] == ID:
                found = True
                print(database[1][i]['Final_grade'])
    elif when == "T":
        found = False
        for i in range(len(database[2])):
            if database[2][i]['Student ID'] == ID:
                found = True
                print(database[2][i]['Final_grade'])
    else:
        # you will have to write the code that goes through all
        # three lists until it finds a match
        pass
    if not found:
        print("That is an error. \n The student was not enrolled in class at that time.")
# no return is necessary

def search_by_last_name(database, name):
    when = get_semester()
    pass

def insert_new_values(students):
    # students is a list of dictionaries
    # each element of the list is a student record; we need to add
    # three new key/value pairs in each dictionary
    for i in range(len(students)):
        students[i]["Project_total"] = int(students[i]["P1"]) + int(students[i]["P2"]) + int(students[i]["P3"])
        students[i]["Total_score"] = int(students[i]["P1"]) + int(students[i]["P2"]) + int(students[i]["P3"]) + int(students[i]["T1"]) + int(students[i]["T2"])+ int(students[i]["T3"])
        if students[i]["Total_score"] >= 576:
            students[i]["Final_grade"] = "A"
        elif students[i]["Total_score"] >= 512:
            students[i]["Final_grade"] = "B"
        elif students[i]["Total_score"] >= 448:
            students[i]["Final_grade"] = "C"
        elif students[i]["Total_score"] >= 384:
            students[i]["Final_grade"] = "D"
        else:
            students[i]["Final_grade"] = "F"

#        print("The student record is ", students[i])

    return students

def plot_bar_graph(database):
    grades = [0, 0, 0, 0, 0]

    for i in range(len(database)):
        for j in range(len(database[i])):
            if database[i][j]["Final_grade"] == 'A':
                grades[0] += 1
            elif database[i][j]["Final_grade"] == 'B':
                grades[1] += 1
            elif database[i][j]["Final_grade"] == 'C':
                grades[2] += 1
            elif database[i][j]["Final_grade"] == 'D':
                grades[3] += 1
            else:
                grades[4] += 1
    plt.bar(GRADES, grades)
    plt.show()


def plot_score_line(database):
    scores = []
    for i in range(len(database)):
        for j in range(len(database[i])):
            scores.append(database[i][j]["Total_score"])
    plt.plot(scores)
    plt.show()
    return scores

def plot_scatter(scores):
    indices = []
    for i in range(len(scores)):
        indices.append(i)
    plt.scatter(scores, indices)
    plt.show()

    

def plot_graphs(database):
    plot_bar_graph(database)
    scores = plot_score_line(database)
    plot_scatter(scores)
#    print(grades)



if __name__ == "__main__":
    database = []
    for file in FILES:
        filename = "/Users/alfredarsenault/PycharmProjects/pythonProject6/Project_2/" + file
        class_rec = read_file(filename) #class_rec is a list of dictionaries
#        print("The file is ",file )
#        print(class_rec)
        class_rec = insert_new_values(class_rec)
        database.append(class_rec)
#    print(database)
    plot_graphs(database)

