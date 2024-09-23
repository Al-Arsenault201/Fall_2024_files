# in-class list related coding from Wednesday, September 18

grocery_list =[]
# an alternative approach
grocery_list = ["Milk", "Eggs", "Strawberries", "apples", "cereal", "cheese"]

#removing an item by its value
#if you try to remove an item that's not there, your
#program will crash
if "Milk" in grocery_list:
    grocery_list.remove("Milk")

# what if we just want to remove the first item in the list
# we use the method "pop"
value = grocery_list.pop(3)
print(value)

# what if we wanted to delete more than one item from the list?
# we could use multiple pop or remove statements

# the del statement
del grocery_list[1:3]#remove two items from the list

# the syntax: grocery_list[1:3]
# the first number is the first element you delete
# the first element gone is grocery_list [1]
# the second number is NOT the last element deleted
# the second number is the FIRST item left

print(grocery_list)
print(len(grocery_list))

# list slicing - take a large list, and select only
# a subset of the items

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
#suppose I want to create a sub-list of only the first ten states
early_states = states[:10]
print(early_states)

#the syntax - [:10]
# if there is no number before the : start at index 0
# start at the beginning of the list
# the second number - 10 - is the index of the first list
# element not included in the slice
# this slice takes states[0], states[1], ..., states[9]
# do not include states[10] - that is the first item
# not included in the slice
next_states = states[10:20]
print(next_states)

