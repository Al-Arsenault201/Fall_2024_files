#in-class coding for Wednesday, October 23

def factorial(n):
    """
    A recursive implementation of the factorial function.
    :param n: a positive integer, whose factorial will be calculated
    :return: n!
    """
    #let's show where we are
    print("\n \n")
    print(" New symbol table: n =", n, " located at ", id(n), "\n\n")
    input("hit enter to continue")
    #first our base case
    if n == 1:
        return 1
    #now our recursive case
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("the answer is: ", factorial(number))

