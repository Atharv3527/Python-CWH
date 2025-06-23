# Tuples are ordered but immutable collections(cannnot be changed after creation)
# At time we will need tuple data structure when we accidently changed the tuple,  but it will not get affected
my_tuple = (10,20,30)
single_element = (5,) # Even tuple with single element requires comma #single element tuple(comma required)

print(my_tuple) # (10,20,30)
print(single_element) # (5,)

a = (3,2,22,13) # (3, 2, 22, 13) not [(3, 2, 22, 13,)]
print(a)
print(a[2])
a[3] = 32
# cannot be changed->tuple object does not support item assignment