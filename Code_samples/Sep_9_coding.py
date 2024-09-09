# this file contains in-class coding
# from Monday, September 9

# input and output
# Output first

#print out your favorite food
#as a literal
print("My favorite food is pizza")

#as a variable
food = "pizza"
print("My favorite food is, ", food)
# use + instead of ,
print("My favorite food is, "+food)

# print ALWAYS prints a new-line/CR when it's
# done UNLESS you use an end=

print("first line")
print("second line")

print ("first line", end="...")
print("second line")

#showing no spaces
print("a line", end="")#no blank spaces
print("another line")

# that's almost all you need to know
# about output in Python

# now input

#we want to interact with a user
# we do this with the 'input' statement

age = input("Enter your age: ")
print ("your age is: ", age)

#the prompt must be a single string
# age = input("Enter your age", "please")

#all input values are treated as strings
"""
new_age = input("please enter your new age: ")
new_age = new_age + 5
print("Your new age is: ", new_age)
"""
#anything that comes in using the input statement
# , comes in as a string

#casting from one type to another
# int( )  changes whatever's in the parens to integer
# float() changes it to a floating point variable
# str() changes it to a string
new_age = int(input("please enter your new age: "))
new_age = new_age + 5
print("Your new age is: ", new_age)