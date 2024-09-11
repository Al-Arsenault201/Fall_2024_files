# In-class coding for conditionals

# sequential execution
name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))
print(name, gpa)

# conditional execution
# execute code only if something is true
if (gpa >= 3.25):
    print("Congrats!")
    print("Again")
    print("Still going")
print("we're done now")

#if - else
# if condition is true do something
# otherwise do something else
if (gpa >= 3.25):
    print("Congrats!")
else:
    print("Sorry, just a little short")