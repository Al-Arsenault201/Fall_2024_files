l1 = ['a','b','c']
l2 = [1,2,3]
print(zip(l1,l2))
d = dict(zip(l1,l2))
print(d)
e = dict(zip(l2,l1))
print(e)
#print(dict(l1,l2))