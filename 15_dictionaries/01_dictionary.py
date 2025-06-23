# Creation of Dictionary
# keys should be hashable - strings,integers,tuples -> lists are not hashable
marks = {"harry": 34,"jack": 45,"lily":94}
print(marks,type(marks)) 
# {'harry': 34, 'jack': 45, 'lily': 94} <class 'dict'>

student = {"name":"Alice","age":21,"grade":"A"}
print(student,type(student)) 
# {'name': 'Alice', 'age': 21, 'grade': 'A'} <class 'dict'>

print(marks["lily"]) # 94
print(student["age"]) # 21
print(student["name"]) # Alice


# Accessing and Modifying Values:
print(student["name"]) # Output: Alice
student["age"] = 22 # Updating Value
student["city"] = 'New York' # Adding new key-value pair
print(student) # {'name': 'Alice', 'age': 22, 'grade': 'A', 'city': 'New York'}