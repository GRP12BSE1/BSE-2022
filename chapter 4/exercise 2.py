def investment(C,r,n,t):
    P=C*((1+(r/n))**(t*n))
    x="{:.2f}".format(P)
    print(f"final value for investment: {x}")

investment(1000,0.01,1,1)
