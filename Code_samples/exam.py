"""

pet = input('enter the name of your pet; enter 0 to stop')
while pet != '0':
   print(pet, " sounds like a wonderful pet")
   pet = input("enter the name of your pet; enter 0 to stop")
"""

def fact(n):
    if n <= 0:
        return -1
    else:
        product = 1
        for i in range(1, n+1):
            product *= i
        return product

if __name__ == '__main__':
    number = int(input('enter the number: '))
    answer = fact(number)
    if answer == -1:
        print("Error - the factorial of a non-positive number is undefined")
    else:
        print(number, " factorial is ", answer)

