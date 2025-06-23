marks = {"harry":34,"jack":45,"lily":94}

# Prints all keys
print(marks.keys()) # dict_keys(['harry', 'jack', 'lily'])
# Prints all values
print(marks.values()) # dict_values([34, 45, 94])

marks.pop("harry") # Removes "harry" key
print(marks) # {'jack': 45, 'lily': 94}
marks.clear() # Empties dictionary
print(marks) # {}