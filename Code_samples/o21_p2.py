with open("/Users/alfredarsenault/Documents/Fall_2021_Project_2/Spring_2022.csv") as infile:
    data = infile.read()
    class_roster = data.split("\n")
    other_class_roster = [ ]

    for i in range(len(class_roster)):
        other_class_roster.append(class_roster[i].split(","))
    print(other_class_roster)