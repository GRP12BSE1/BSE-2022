while True:
    try:
        fname = input("enter filename: ")
        fhand = open(fname)
    except:
        print("Invalid file!")
        continue
    break
sum = 0
count = 0
for words in fhand:
        if words.startswith("X-DSPAM-Confidence:"):
            y = words
            w = y[20:]
            w = float(w)
            sum += w
            count += 1

print(sum/count)