# in class coding for Monday, September 23

#get the user to type in two integers
#print out the even numbers between those two
start=int(input("enter the lower number"))
end = int(input("enter the upper number"))

for i in range(start,end):
    if i % 2 == 0:
        print(i)

