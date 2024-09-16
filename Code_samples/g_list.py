# the grocery list program from Sept 16

grocery_list = []  # square brackets
#empty list
# one way to add an item
grocery_list.append("Milk")
grocery_list.append("eggs")
grocery_list.append("Broccoli")

# insert a value in a specific place in the list
grocery_list.insert(0,"grapes")

# remove an item from the list
grocery_list.remove("grapes") # removes by value

# what if the item isn't there
grocery_list.remove("Lactaid")
# if the item's not in the list, the program will crash
# in
if ("Lactaid" in grocery_list):
    grocery_list.remove("Lactaid")


#code to show how this works
print(grocery_list) #prints the entire contents of the list
print (len(grocery_list)) #len returns the length of the list

print(grocery_list[0])
print(grocery_list[1])
#print(grocery_list[len(grocery_list)-1])
print(grocery_list[-1]) # the last element in the list

#mutability
a = 5
id(a)
a *= 3
print(a)
id(a)