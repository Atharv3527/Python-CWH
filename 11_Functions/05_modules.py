# Two types of modules in Python:
# - Built in Modules
# - External Modules
# list of built in modules in python from python docs
# https://docs.python.org/3/library/builtins.html
import math
import os
import mymodule 
import requests #pip install requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text) # html code of google