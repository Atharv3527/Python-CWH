def sum(*args):
    # args will be a tuple of all the values passed to sum
    # print(args)
    total = 0
    for items in args:
        total+=items
    return total

'''
# sum(342,2,7) #(342, 2, 7)
# print(sum(342,2,7)) #(342, 2, 7) \n None

'''

# print(sum(342,4,5,9)) 
# #360

def greet(*args):
    for name in args:
        print(f"Hello {name}!")

greet("Vedant","Deepak","Vinay") 
# Hello Vedant!
# Hello Deepak!
# Hello Vinay!