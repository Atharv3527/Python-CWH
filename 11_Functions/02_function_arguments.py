def add(a,b,plus=0): #Here a and b are parameters
    x = a + b+plus
    return x

ans1 = add(2,6,2) #only return functions value can be stored in a variable #arguments
#value gets overidden plus gets converted to 2
print(ans1) #10

c1  = add(b=5,a=3)
print(c1)#8