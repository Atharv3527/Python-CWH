#Lists are ordered,mutable collections of items # mutable - can be changed after creation
marks = [54,23,64,93,32]
mixed = [10,"hello",3.14,False]
#Lists are mutable
print(marks)
print(mixed)

# Accessing the value through index just like strings
print(marks[2]) # 64
print(mixed[1]) #"Hello"

# Trying slicing in lists
print("Through Slicing of given lists")
print(marks[2:4])
print(mixed[0:5]) #[10,"hello",3.14,False]
print(mixed[2:5]) #[3.14,False]
print(mixed[5]) # Indexing out of range error,Index out of bound

