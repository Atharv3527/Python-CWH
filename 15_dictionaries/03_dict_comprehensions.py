# Dict comprehension ->
#  Table of 5

table_5 = {i:i*5 for i in range(1,11)}
print(table_5) # {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}

#Squares of a number
squares = {x:x**2 for x in range(0,6)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
