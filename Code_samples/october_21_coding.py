# in-class coding from Monday, October 21

with open("/Users/alfredarsenault/PycharmProjects/pythonProject6/part3_data.txt", "r" ) as infile:
    data = infile.read()
    print(data)
    data_list = data.split("\n")
    print(data_list)
    for i in range(len(data_list)):
        data_list[i] = list(data_list[i])
        print(data_list[i])
    print(data_list)
