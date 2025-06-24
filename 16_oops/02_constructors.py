class Employee:

    # pass -> used when we want to code it later
    def __init__(self,salary,name,bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        

    def get_salary(self): #self is important here because self is a way to reference the object of the class which is being created
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.Salary is {self.salary} and The bond is for {self.bond} years")
    
e1 = Employee(34000,"John Doe",4)
# print(e1.get_salary())
e1.get_info()