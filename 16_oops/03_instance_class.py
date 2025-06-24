class Employee:
     
    company = "Asus" # This is class attribute
    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
        

    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.Salary is {self.salary} and The bond is for {self.bond} years")

e1 = Employee(120000,"Atharv",2,"Tesla")
# e1.get_info()
# e1.company = "Tesla"
# print(e1.get_salary())
print(e1.company) # will always print instance attribute whenver present, if not present will print the class attribute

print(Employee.company) # Way to print the class Attribute


# Object introspection
# print(dir(e1)) # To find out all attributes and methods that a particular object has ..