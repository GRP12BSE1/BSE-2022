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
    M = max(a)
    m = min(a)
    C = len(a)
    print(S, M, m, C)
    break
