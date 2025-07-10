numbers = [1,2,3,45,4,21]

# def square(x): #can be replaced by lambda function
#     return x*x

new = list(map(lambda x: x*x,numbers)) #It will iterate through each element of the list numbers
print(new)