# in class coding from Monday, September 23

for i in range(0,4,1): #range(0,4) if there are only two values
        # they are the initial, and terminator - hop count is 1
    for j in range(0,4,1): #range(4) if there's only one value
        # it's the terminator - start at 0, hop count is 1
        print(i*j, end=" ")
    print("\n")

int_list = [1,2,3,4,5]
for number in int_list:
    #you can't change the value of the original list
