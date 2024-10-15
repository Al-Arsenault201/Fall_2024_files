# in-class coding for Monday, October 14

dogs = {'doug':['beagle','English bulldog'],
         'lizzie':'australian cattle dog',
         'wesley':['german shepherd', 'boxer'],
        'bentley':['australian cattle dog','chow', 'golden retriever']
        }

#what kind of dog is 'doug'?
print(dogs["doug"])

#can you access elements of a dictionary by value?
#no - not directly
for key in dogs.keys():
    if dogs[key] == "australian cattle dog":
        print(key)

# do I have any spaniels?
if "spaniel" in dogs.values():
    print("yes, there are ")
else:
    print("Sorry, no spaniels")

#let's add a dog
dogs["penny"]="spaniel"
if "spaniel" in dogs.values():
    print("yes, there are ")
else:
    print("Sorry, no spaniels")

# oops - we had wesley's type wrong; he's just a german shepherd
# change the value
dogs["wesley"] = "german shepherd"

# SUPPOSE we discover doug is also part boxer
# add that to the list
dogs["doug"].append("boxer")
print(dogs["doug"])

#dogs["lizzie"].append('lab')

#print(dogs['baron'])
print(dogs.get("baron"))
print(dogs.get("baron","sorry that's an error"))
