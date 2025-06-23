#Create a list containing the table of 5

table = []
for i in range(1,11):
    table.append(5*i)
print(table)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

#Another way -> comprehension way
table_5 = [x*5 for x in range(1,11)]
print(table_5) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


marks = [x**2 for x in range(5)]
print(marks) # [0, 1, 4, 9, 16]