while True:
    filename = input("enter file: ")
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        try:
            fhand = open(filename)
        except:
            print("File cannot be opened:", filename)
            continue
        break

count = 0
for word in fhand:
    count = count + 1
print("There are", count, "subject lines in", filename)