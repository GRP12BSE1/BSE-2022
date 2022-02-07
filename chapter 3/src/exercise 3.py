num = input("Enter score:")
try:
    score = float(num)
    if score > 1.0 or score < 0:
        print("Bad score entered")
    else:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
except:
    if num == "done":
        print(done)
    else:
        print("Wrong value it should be a float")


