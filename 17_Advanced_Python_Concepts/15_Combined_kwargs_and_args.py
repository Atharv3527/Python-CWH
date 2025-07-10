def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,3,4,5,Atharv = 97,BOB = 89,Shubham = 78)


print("------------------------------------------------------>")

def info(*args,**kwargs):
    print("args",args)
    print("kwargs",kwargs)

info("Atharv",13,name="Harry",lang="Python")
# args ('Atharv', 13)
# kwargs {'name': 'Harry', 'lang': 'Python'}