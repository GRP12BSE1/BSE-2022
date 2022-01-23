X = float(input("Enter an amount to make change for: "))
print("Your change is...")
if X >= 20:
    print(str(int(X // 20)) + " Twenties")
else:
    print("0 Twenties")
X = X % 20
if X >= 10:
    print(str(int(X // 10)) + " Tens")
else:
    print("0 Tens")
X = X % 10
if X >=5:
    print(str(int(X // 5)) + " fives")
else:
    print("0 fives")
X= X % 5
if X >= 1:
    print(str(int(X // 1)) + " Ones")
else:
    print("0 ones")
X = X - int(X)
if X >= 0.25:
    print(str(int(X // 0.25)) + " Quarters")
else:
    print("0 Quarters")
X = X % 0.25
if  X >= 0.1:
    print(str(int(X // 0.1)) + " Dimes")
else:
    print("0 dimes")
X = X % 0.1
if X >= 0.05:
    print(str(int(X // 0.05)) + " nickels")
else:
    print("0 nickels")
X = X % 0.05
if X >=0.01:
    print(str(int(X // 0.01)) + " pennies")
else:
    print("0 pennies")
