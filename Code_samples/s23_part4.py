
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


# print out the name of every state that ends in a

for state in states:
    if state[-1].lower() == "a":
        print(state)

#print out every state that ends in a vowel
VOWELS = ['a','e','i','o','u','y']
for i in range(len(states)):
    if states[i][-1] in VOWELS:
        # if states[i][-1] == 'a' or states[i][-1] == 'e' or
        # states[i][-1] == "o" or,,,
        print(i,'\t', states[i])

#how do I check to see if the user entered an integer
is_num = True
age = input("Enter your age: ")
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for character in age:
    if not(character in digits):
        is_num = False
if is_num == True:
    print(int(age))