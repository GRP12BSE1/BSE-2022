while True:
    try:
        filename = input("enter file: ")
        fhand = open(filename)
    except:
        print("Invalid file!")
        continue
    break

count = 0
for word in fhand:
    if word.startswith("From "):
        word = word.split()
        count = count + 1
        print(word[1])
print("There were", count, "lines in the file with From as the first word")