
import random

def roll_dice( ):
    roll = []
    for i in range(5):
        roll.append(random.randint(1,6))
    print("roll = ", roll)
    return roll

def count_num(roll):
    results = [0,0,0,0,0,0]
    for i in range(len(roll)):
        results[roll[i]-1] += 1
    print(results)
    return results


def check_pytzee(results):
    if 5 in results:
        return True
    else:
        return False

def check_3_4(results):
    if 4 in results:
        for i in range(len(results)):
            if results[i] == 4:
                return 4 * (i+1)
    elif 3 in results:
        for i in range(len(results)):
            if results[i] == 3:
                return 3 * (i+1)
    else:
        return 0

def type_hand(results):
    if 5 in results:
        return "pytzee"
    elif 4 in results:
        return "four"
    elif 3 in results:
        if 2 in results:
            return "full house"
        else:
            return "three"
    elif (results[0]==1 and results[1]==1 and results[2]==1 and results[3]==1 and results[4]>=1) or (results[1]>=1 and results[2]>=1 and results[3]>=1 and results[4]>=1 and results[5]>=1):
        return "large straight"
    for i in range(0,3):
        if results[i] > 0 and results[i+1]>0 and results[i+2]>0 and results[i+3]>0:
            return "small straight"
    return "count_number"

def compute_new_score(score, type_string, results):
    if type_string=="pytzee":
        score += 50
        return score
    elif type_string=="four":


def play_game(num_rounds):
    score = 0
    for i in range(num_rounds):
        roll = roll_dice()
        num_each = count_num(roll)
        print(type_hand(num_each))
        print("\n")
        print("\n")


#        if check_pytzee(num_each):
#            score += 50
#        elif check_3_4(num_each) != 0:
#            score += check_3_4(num_each)
#        print(score)



if __name__ == "__main__":
    num_rounds = int(input("How many rounds do you want to play?"))
    seed = int(input("enter a seed; enter 0 to skip"))
    if seed != 0:
        random.seed(seed)
    play_game(num_rounds)

