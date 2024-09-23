# in-class coding for Monday, September 23, 2024'

grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples",
                "Strawberries", "Broccoli", "Cucumber",
                "Tomatoes", "Green Onions"]

# print out each element of the list
# one item per line

#for "each" loop

for item in grocery_list:
    item = item+"TAIL"
    print(item)
print(grocery_list)
# item gets set to each value in the list
# in order, one time

# more general - for i loop:

for i in range(0,len(grocery_list), 1):
    grocery_list[i] = grocery_list[i]+"ITEM"
    print(grocery_list[i])
print(grocery_list)

#if you want to change the values in the original list
# you cannot use a for each; you must use for i
