# summing the integers in a list recursively

def sum_numbers(numbers):
    print(len(numbers), "elements left")
    input()


    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_numbers(numbers[1:])

def iterative_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(sum_numbers(numbers))