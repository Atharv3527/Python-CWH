#Set Operations:
a = {1,2,3}
b = {3,4,5}

s = a.union(b)
print(s) # {1, 2, 3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5} # Contains all elements in a along with all the elements in b
print(b.union(a)) # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3} # Contains only the elements that are present in a as well as b
print(b.intersection(a)) # {3}
print(a.difference(b)) # {1, 2}
print(b.difference(a)) # {4,5}
 
# Use Case: Sets are great for eliminating duplicate values.