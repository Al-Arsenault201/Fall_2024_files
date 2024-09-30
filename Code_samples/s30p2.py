
def factorial(n):
    # n>0 and is an integer
    product = 1
    for i in range(1, n+1):
        product *= i
    print(product)

if __name__ == '__main__':
    value = int(input("enter a positive integer and I'll calculate the factorial of it: "))
    print(factorial(value))

