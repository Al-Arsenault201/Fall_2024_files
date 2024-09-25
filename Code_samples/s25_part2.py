
#ask the user for an integer between 1 and 12 inclusive
num = int(input("enter a number between 1 and 12 inclusive"))
while (not (num >= 1 and num <= 12)):
    print("We really need an integer between 1 and 12 inclusive")
    num = int(input("enter a number between 1 and 12 inclusive"))
print(num)
"""
num = 1
while num != 100:
    print(num)
    num += 2

print("Done")
"""
print("This program asks for President names")
print("Enter Q to quit")
# Q is the "sentinel"
pres = input("Enter the next name")
while pres.upper() != 'Q':
    print(pres)
    pres = input("Enter the next name")

# encountered the sentinel; done with the loop
print("Thank you")
