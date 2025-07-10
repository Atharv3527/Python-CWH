nums = [1,3,5,234,34,32,6543,23,2,5,16,17,43]

def is_greater_than_9(x): #This can be also replaced by lambda function
    if x>9:
        return True
    else:
        return False
    
new_nums = list(filter(lambda x:x>9,nums)) 
#If the function is more complex and can't be readable then don't prefer the lambda function depicts the bad code behaviour
print(new_nums)