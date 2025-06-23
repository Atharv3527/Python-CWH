s = {34,23,1,3,22}

print(s) # {1, 34, 3, 22, 23}

# can be added anywhere
s.add(32)
print(s) # {32, 1, 34, 3, 22, 23}
s.add(322)
print(s) # {32, 1, 34, 3, 322, 22, 23}
s.remove(1)
print(s) # {32, 34, 3, 322, 22, 23}

# s.remove(34533) # Throws an error
# print(s)#KeyError: 34533, Element not present in set

s.discard(2345) # Function->Remove the respective passed element only if present or be silent->will not represent error eventhough element not present in set
print(s)

s.pop() # Removes random element
print(s)