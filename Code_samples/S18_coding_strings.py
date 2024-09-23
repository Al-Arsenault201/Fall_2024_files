# string-related coding from Wednesday, September 18

# strings are not lists
# but you can do many of the same things with strings that
# you can do with lists
# you cannot change the value of a string variable
# you MUST reassign
#college = "Purdue University"
#print(id(college))
college = "UMBC"  # reassigning
#print(id(college))

#things you can do with strings
# can you calculate length?

print(college)
print(len(college)) #the length of a string is the number of characters in the string
# can it be zero?
#print(len(""))
#can we reference an individual letter in a string?
print(college[0])
#can we slice a string?
print(college[:-1]) #this is called string slicing

#but we cannot change elements in a string
#here's a list:
college_list = ["UMBC","UMCP","Johns Hopkins","Towson"]
college = "UMBC"
print(college_list)
print(college)
#I can change the list - because lists are mutable
college_list[1] = "Salisbury"
print(college_list)
#I cannot change the string
#college[2] = "H"
college = "UMHC" #I haven't changed the string; I reassigned it
print(college)

# split and join - almost opposites
#split takes a string and returns a list
# join takes a list of strings and returns a single string

# split cuts up the string on a character you define
# by default - white space - blanks, tabs, newlines
mystring = "Every once in a while a good thing happens"
mystringlist = mystring.split()
print(mystringlist)

#what if we want to split on something other than whitespace?
newstringlist = mystring.split("e")
print(newstringlist)

#join
mylist = ["a","b","c","d"]
s = "".join(mylist)
print(s)
t = " ".join(mylist)
print(t)
u = ",".join(mylist)
print(u)
#join only works with lists of strings
nums = [1,2,3,4]
strn = ",".join(nums)
print(strn)