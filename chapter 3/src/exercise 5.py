x = int(input("Enter number of attendies: "))
if x>200:
    print("$20,000")
elif 100<x<=200:
    print("$15,000")
elif 50<x<=100:
    print("$10,000")
else:
    print("$4,000")