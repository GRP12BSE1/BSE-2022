C = float(input("C: "))
r = float(input("r: "))
n = float(input("n: "))
t = float(input("t: "))

def investment(C,r,n,t):
    P=C*((1+(r/n))**(t*n))
    x="{:.2f}".format(P)
    print(f"final value for investment: {x}")

investment(C,r,n,t)

