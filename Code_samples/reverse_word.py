# in class programming from September 30

# reversing a word

def reverse_word(word):
    """
    function: reverse_word
    purpose: take a string and return it in reverse order
    :param word: the string we want to reverse
    :return: none in this case
    """
    i = 0
    reversed_word = ''  # Do not use the function name here!!!!
    while i < len(word):
        reversed_word = reversed_word + word[len(word)-i-1]
        i += 1
    print(" The word ", word, " reversed is ", reversed_word)

def return_reverse_word(word):
    """
    function: reverse_word
    purpose: take a string and return it in reverse order
    :param word: the string we want to reverse
    :return: none in this case
    """
    i = 0
    reversed_word = ''  # Do not use the function name here!!!!
    while i < len(word):
        reversed_word = reversed_word + word[len(word)-i-1]
        i += 1
    #print(" The word ", word, " reversed is ", reversed_word)
    return reversed_word



if __name__ == '__main__':
    word = input("Enter a string: ")
    t = reverse_word(word)
    print(t)
    s = return_reverse_word(word)
    print(s)
