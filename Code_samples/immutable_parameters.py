#  First the function definition
def reverse_word(word):
    i = 0
    reversed_word = ""
    print(id(reversed_word))
    print("animals are",animals)
    while i < len(word):
        reversed_word += word[-(i+1)]
        i += 1
    return reversed_word


#	word = reversed_word

if __name__ == "__main__":
    # Now the call is
    animals =["cat", "Australian cattle dog", "duckbilled platypus",
        "ocelot", "zebra"]
    for critter in animals:
        print(id(critter))
        reverse_word(critter)
        print(critter)
    # now do whatever you want to with the
    # reversed word in the main program



