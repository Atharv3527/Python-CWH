# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The division is {a/b}")
#     except ValueError:
#         print("Please dont perform bad typecasts")
    
#     except ZeroDivisionError:
#         print("Hey don't divide by 0")

#     except Exception as e:
#         print("Unknown Error occured!",e)

#Raising method = Custom one
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b==0:
    raise ValueError("Please dont divide by 0")
#The program collapses by displaying -> ValueError: Please dont divide by 0

print(f"The division is {a/b}")