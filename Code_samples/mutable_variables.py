
def reverse_word(word_list):
    j = 0
    print(id(word_list))
    for j in range(len(word_list)):
        i = 0
        reversed_word = ""
        while i < len(word_list[j]):
            reversed_word += word_list[j][-(i+1)]
            i += 1
        word_list[j] = reversed_word
#    return word_list

if __name__ == '__main__':
    animals = ["cat", "Australian cattle dog", "duckbilled platypus",
        "ocelot", "zebra"]
    print(id(animals))
    reverse_word(animals)
    print(animals)

