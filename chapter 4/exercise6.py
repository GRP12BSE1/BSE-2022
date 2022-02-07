hours = float(input("Enter Hours "))
rate = float(input("Enter Rate "))

def compute_pay(hours,rate):
    if hours > 40:
        extra_hours = hours - 40
        pay = (1.5 * rate * extra_hours) + (40 * rate)
        print(pay)
    else:
        new_pay = hours * rate
        print(new_pay)
print(compute_pay(hours,rate))


