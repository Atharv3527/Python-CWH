class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    #Instance method (default)
    def print_info(self):
        info =  f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    #static method used when wants to process without self
    @staticmethod
    def sum(a,b):
        return a+b
    
    #class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = Employee("Jack",3455)
e2 = Employee("Jill",34355)

# print(Employee.company)
# print(Employee.name) #This will throw an Error
e1.print_info()
e2.print_info()

# print(e2.sum(5,23)) #Error
print(Employee.company) #Employee=e1
e1.change_company("Acer")
print(Employee.company) #Employee=e1


#It changes the class variable not instance variable

#Work upon class variable and instance variable