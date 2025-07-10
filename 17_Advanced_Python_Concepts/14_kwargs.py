def introduce(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=25, city="Pune")
# name: Alice
# age: 25
# city: Pune

print("------------------------------------->")
def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks
    for key,value in kwargs.items():
        print(f"{key}: {value}")

marks(atharv = 98,vedant = 89,sahil = 89)
print("------------------------------------->")
def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} are {kwargs[item]}")

marks(Shubham = 78,milind = 89,jack = 45,marie = 90,priya = 55)