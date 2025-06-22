def sum(a,b):
    print("Hey I am summing")
    c = a + b
    global z #Please modify global z
    z = 0 # This will refer to global z and not create a local variable
    return c
z = 3
print(z)
print(sum(3,2))
print(z)

# This allows functions to change global variables,but excessive use of global is discouraged as it can make debugging harder.