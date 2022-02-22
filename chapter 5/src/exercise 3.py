print(">"*3)
print("="*15)
print("RESTART")
print("="*15)
print(">"*3)
print("Welcome to the vending machine change maker program \nChange marker initialized")

a = [25, 25, 25, 0, 0]
b = ["nickels", "dimes", "quarters", "ones", "fives"]
c =["'n'", "'d'", "'q'", "'o'", "'f'", "'c'"]
d = ["deposit a nickel", "deposit a dime", "deposit a quarter", "deposit a one dollar bill", "deposit a five dollar bill", "cancel the purchase"]
e = [0.05, 0.1, 0.25, 1, 5]
count= 0
def start(a,b):
    print("\nStock contains: ")
    for i in range(len(a)):
        print(a[i], "-", b[i])
    return identifying_purchase_price(a)
def identifying_purchase_price(a):
    user_input = input("\nEnter the purchase price (xx.xx) or `q' to quit:")
    if user_input == "q":
        t = (a[0]*0.05 + a[1]*0.1 + a[2] * 0.25)
        q = (a[4]*5 + a[3]*1)
        if t*100 >= 100:
            q += t//1
            t -= t//1
        print("Total: {0} dollars and {1} cents".format( q, int(t*100) ))
    else:
        if user_input != " ":
            if user_input != "":
                try:
                    checked_input = round(float(user_input), 2)
                    a = ((checked_input * 100) // 5)
                    if (((checked_input * 100)) - (a * 5)) == 0:
                        return deposit_menu(), depositing(checked_input)
                    else:
                        print("Illegal price: Must be a non-negative multiple of 5 cents.")
                        return identifying_purchase_price(a)
                except:
                    return identifying_purchase_price(a)
            else:
                print("Illegal price: Must be a non-negative multiple of 5 cents.")
                return identifying_purchase_price(a)
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
            return identifying_purchase_price(a)
def deposit_menu():
    print("\nMenu for  deposits")
    for i in range(len(c)):
        print(c[i], "-", d[i])
def depositing(y):
    balance = y
    while round(balance, 2) > 0:
        print("\nPayment due: {0} dollars and {1} cents".format(int(balance), int(round(((balance - int(balance)) * 100), 0))))
        deposit = input("Indicate your deposit:")
        for ( i , v ) in enumerate(["n", "d", "q", "o", "f"]):
            if deposit == v:
                a[i] += 1
                balance -= e[i]
                if balance <= 0:
                    return returning_change( abs(balance) , 0)
        if deposit == "c":
            return returning_change(y, balance)
        elif deposit not in "ndqofc":
            print("Illegal selection:", deposit)
def returning_change(s, v):
    print("\nPlease take the change below")
    cummulative_addition = s - v
    cummulative_manager = 0
    if cummulative_addition == 0:
        print("No change due\n")
        return "\n", start(a, b)
    remainder = 0
    while round(cummulative_addition, 2) >= 0:
        for (i) in range(3):
            g = 0
            z = round(cummulative_addition, 2) / e[2 - i]
            if round(cummulative_addition, 2) != 0:
                if z <= a[2 - i]:
                    g = z - int(z)
                    if int(z) > 0:
                        print(int(z), b[2 - i],)
                    cummulative_addition -= z * e[2 - i]
                    a[2 - i] -= int(z)
                    if g != 0:
                        cummulative_manager += e[2 - i] * g
                        cummulative_addition += e[2 - i] * g
                elif z > a[2 - i]:
                    print(a[2 - i], b[2 - i],)
                    cummulative_addition -= a[2 - i] * e[2 - i]
                    a[2 - i] -= a[2 - i]
        break
    remainder = round(cummulative_addition, 2)*100
    if round(cummulative_addition, 2) > 0:
        if remainder != 0:
            real_dollar = 0
            if int(remainder) >= 100:
                real_dollar += remainder // 100
                remainder %= 100
                print("Machine is out of change.\nSee store manager for remaining refund.\nAmount due is: {0} dollars {1} cents".format(real_dollar , remainder))
            else:
                print("Machine is out of change.\nSee store manager for remaining refund.\nAmount due is: {0} cents".format(int(remainder)))
        return "\n" , start(a,b)
    else:
        return start(a,b)
start(a,b)
