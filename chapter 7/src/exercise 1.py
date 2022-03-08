fname = input("enter filename: ")
fhand = open(fname)
file = fhand.read()
print(file.upper())