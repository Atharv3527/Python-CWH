
def divide(a,b):
    try:
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    #This is always executed no matter if try completely executes or not #finally used in functions
    finally: #try to remove finally and execute
        print("This is always executed")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

divide(a,b)


'''
1st program :-

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
    c = a/b
    print(c)
    return c

except Exception as e:
    print(e)
    return None

#This is always executed no matter if try completely executes or not #finally used in functions
#try to remove finally and execute
print("This is always executed") #This gets always executed then why to use finally explanation given above
'''