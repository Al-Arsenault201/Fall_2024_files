#how to do step 1
#read in one file and create a 2d list of student records
#and then a list of dictionaries

def convert_student_to_dict(student):#student is the student record as a list
    s = {}
    s["last_name"] = student[0]
    s["first_name"] = student[1]
    s["student_id"] = student[2]
    #there are six more key-value pairs
    return s

def read_file(fname):
    class_list = []
    with open(fname,"r") as infile:
        infile.readline()
        infile.readline()
        data = infile.readlines()#now I have the data in this list
 #       print(data)
        for i in range(len(data)):
            data[i] = data[i].split(",")
     #       print(data[i])
     #       clean up the " characters I don't need
            for j in range(len(data[i])):
                data[i][j] = data[i][j].replace('"','')
   #        print(data[i])
            student_dict = convert_student_to_dict(data[i])
            class_list.append(student_dict)
        return class_list

if __name__ == "__main__":
    filename = "Fall_2025.csv"
    class_list = read_file(filename)
    print(class_list)