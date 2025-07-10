#write to a file called John Doe.txt.
#It should contain data about John Doe

f = open("John Doe.txt","w")


# ''' "String Content" ''' = python multlines
string = '''
John Doe is a nice guy. He lives in Nyc and he works with python His favourite package is Pandas
'''

f.write(string)
f.close()

#w = wipes out the content of the intial content on the mentioned file and writes over it
#a = it appends the content to initial  mentioned file content