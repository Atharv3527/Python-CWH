# Class: Class is a blueprint or a template.Eg. form for an Exam that contains name,age,electives,father's name etc

# Object: Specific instance created from the template (class.). Eg. form which contains the data for John Doe

class Employee:
    company = "HP"

    def get_salary(self): # self - it is a reference to the objcet of the class which is being created,so self is a way to reference the object of the class which is being created.
        # print(self)
        return 34000


e1 = Employee() # An object of class Employee is created here
print(e1.get_salary()) #34000 -> Employee's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)
