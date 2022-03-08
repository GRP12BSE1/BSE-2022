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

    M = max(a)
    m = min(a)
   
    print("Maximum: ", M)
    print("Minimum: ", m)
    break
