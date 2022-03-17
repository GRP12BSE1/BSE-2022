while True:
    filename = input("enter file: ")
    try:
        fhand = open(filename)
    except:
        print("File not found. Try again.")
        continue
    break

words = []
for line in fhand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        words.append(word)
a = sorted(words)
uniques = []
for word in a:
    if word not in uniques:
        uniques.append(word)
print(uniques)


