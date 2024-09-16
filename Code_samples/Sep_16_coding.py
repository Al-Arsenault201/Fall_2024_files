# Monday, September 16
# a quick explanation of Part 5, HW2
month = int(input("Enter the number of a month; 1 is January and 12 is December"))
if (month <1 or month>12):
    print("That is not a valid month")
else:
    if (month == 1):
        print("January")
"""        
    else:
        if (month == 2):
            print("February")
        else:
            if (month == 3):
"""
    elif (month == 2):  # else if month ==2
        print("February")
    elif (month == 3):
        print("March")
    elif (month == 4):
        print("April")
    else:
        print("Not one of those")