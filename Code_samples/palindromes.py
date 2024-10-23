# recursively compute whether a string is a palindrome
# whether it is identical forward and backward
# assume lower-case only

#recursive function
def check_pal (s):
    """
    recursive function to see if s is a palindrome
    :param s: string
    :return: boolean
    """
# what is our base case?
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return check_pal(s[1:-1])

if __name__ == "__main__":
    test_string = input("Enter a string to be tested: ")
    answer = check_pal(test_string)
    print(answer)