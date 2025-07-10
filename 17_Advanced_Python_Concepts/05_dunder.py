# dunder == double underScore

class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self): #Used mainly by the developers in development
        return f"name: {self.name}\nsalry: {self.salary}"
    
    def __len__(self):
        return len(self.name)

e = Employee("Harry",43566)
# print(e.name,e.salary)
# print(str(e)) #The name is Harry and the salary is 43566
# print(repr(e))
# # name: Harry
# # salry: 43566
print(len(e)) #5