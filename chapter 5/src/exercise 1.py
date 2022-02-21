while True:
    try:
        a = []
        while True:
           N = input("Enter number: ")
           if N == "done".lower():
            break
           N = a.append(float(N))

    except:
            print("INVALID INPUT")
            continue
    S = sum(a)
    A = sum(a)/len(a)
    C = len(a)
    print(S, A, C)
    break
