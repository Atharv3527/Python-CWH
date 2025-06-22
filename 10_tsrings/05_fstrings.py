#String formatting

# template = "Dear Harry, You are awesome. Take this 10000$ bag"


template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1 = 300

s1 = template.format(a,a1)
print(s1)

#optimization
print(f"{a} you are awesome and take this {a1}$ bag")

#ord() and chr() -Character Encoding
text = "Hello, Python!" #Depending on ASCII Value
print(ord('A')) #Output: 65
print(chr(65)) #Output: 'A'
