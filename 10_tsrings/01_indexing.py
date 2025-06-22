name = "Atharv"

#name ="A  t  h  a  r  v"
#       0  1  2  3  4  5
#      -6 -5 -4 -3 -2 -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6]) # Eroor->IndexError: string index out of range 


#It is Basically = [length - (Negative Index)]
print(name[-1]) #name[5] = name[6-1]
print(name[-2]) #name[4] = name[6-2]
print(name[-3]) #name[3] = name[6-3]
print(name[-4]) #name[2] = name[6-4]
print(name[-5]) #name[1] = name[6-5]
print(name[-6]) #name[0] = name[6-6]