#in-class coding from Wednesday, September 25

solution = input("enter the solution word")
guess = input("Enter the guess")

answer = []
for g in guess:
    if g in solution:
        answer.append("y")
    else:
        answer.append("_")
for i in range(len(guess)):
    if guess[i] == solution[i]:
        answer.append("g")
    elf
