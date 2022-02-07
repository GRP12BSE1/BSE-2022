try:
    hour = float(input("Enter hour: "))
    rate = float(input("Enter rate: "))
except ValueError:
    print("Error, please enter numeric input")