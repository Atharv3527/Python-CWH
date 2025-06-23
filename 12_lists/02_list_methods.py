marks = [5,2,21,5,7]
'''
Methods-> 1)append
          2)insert
          3)remove
          4)pop
          5)sort
          6)reverse
          7)extend
'''
print(marks) 
marks.append(99) #[5, 2, 21, 5, 7, 99] 
marks.append(6)  # [5, 2, 21, 5, 7, 99,6] 
print(marks) 
marks.insert(99,100) # [5, 2, 21, 5, 7, 99, 6,100] #(after_which_Element,new_Element)
print(marks)
marks.remove(5) # Removes the first occurence of that element
print(marks) # [2, 21, 5, 7, 99, 6,100]

# Append->insert->remove

# newMarks = marks.sort()
# print(newMarks) # Not possible gives "None" as an output
marks.sort() # [2, 5, 6, 7, 21, 99, 100]
print(marks)

marks.reverse() # [100, 99, 21, 7, 6, 5, 2]
print(marks)
marks.pop() # [100, 99, 21, 7, 6, 5]
print(marks)

# extend method
new_marks = [690,720]
marks.extend(new_marks) # [100, 99, 21, 7, 6, 5, 690, 720]
print(marks)
