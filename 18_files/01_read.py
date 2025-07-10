f = open("atharva.txt", "r") #rt = read file in text mode & rb = read file in binary mode #If this don't work then use below one
# f = open("D:/Python course CWH/18_files/atharv.txt", "r")

content_of_file = f.read()
print(content_of_file)
f.close()