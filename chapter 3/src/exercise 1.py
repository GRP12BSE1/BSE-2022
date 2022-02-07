hour = float(input("Enter Hours "))
rate = float(input("Enter Rate "))
if hour>40:
    extra_hours = hour-40
    pay = (1.5*rate*extra_hours)+(40*rate)
    print(pay)
else:
    new_pay=hour*rate
    print(new_pay)

