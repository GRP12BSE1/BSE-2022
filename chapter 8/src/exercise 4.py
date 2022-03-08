while True:
    filename = input("enter file: ")
    try:
        fhand = open(filename)
    except:
        print("File not found. Try again.")
        continue
    break

words = []
for word in fhand:
    word = word.rstrip()
    word = word.split()
    for i in word:
        words.append(i)
print(sorted(words))



