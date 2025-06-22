# name = "Atharv" # strings are immutable
# # Always Keep in mind that you cannot change the actual string in memory
# # name[0] = "R" # You cannot do this Error -> 'str' object does not support item assignment

# a = len(name) #returns length of a string
# print(a)

# 1)Changing Case
# s = "hello world"
# a = len(s)
# print(a) #It also counts the blank spaces
# print(s.upper(),s) #Orginal string remains same
# print(s.lower()) 
# print(s.capitalize()) #capitalize only first letter of a given string
# print(s.title()) # return a version of the string where each word is titlecased # -> Hello World


# 2)Removing Whitespace
# strip() -> removes leading and trailing whitespaces from a string
# text = " hello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# text = " \nhello world "
# print(text.strip()) # Output: "hello world" (removes\n)
# print(text.lstrip()) # Output: "hello world "
# # (removes\n)
# print(text.rstrip()) # Output: " hello world" (do not removes\n)


# 3)Finding and Replacing
# text = "Python is fun"
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun","awesome")) #Python is awesome

# text = "Python is fun and fun and fun"
# print(text.replace("fun","awesome"))
#Output : Python is awesome and awesome and awesome


# 4)Splitting and Joining
# text = "Apples,Bananas,Pineapples"
# print(text.split(",")) #Output - ['Apples', 'Bananas', 'Pineapples']
# print(",".join(['Apples','Bananas','Pineapples']))
# #output = Apples,Bananas,Pineapples


text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) #Output: False
print(text.isalnum()) #Output: True
print(text.isspace()) #Output: False


text1 = "   "
print(text1.isspace())   # True — because all characters are spaces

text2 = "  \n\t  "
print(text2.isspace())   # True — contains spaces, newline and tab only

text3 = "Hello World"
print(text3.isspace())   # False — contains letters

text4 = ""
print(text4.isspace())   # False — empty string

text5 = " t "
print(text5.isspace())  #False