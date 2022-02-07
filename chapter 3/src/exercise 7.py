place = input("Enter the location:").lower()
amount = int(input("Enter the amount:"))
if place == "mbarara":
    if amount > 4000000:
        print("Decision: 'Without a doubt, I'll take it")
    else:
        print("No thanks, I can get something better")
elif place == "kampala":
    if amount > 10000000:
        print("Decision: 'Without a doubt, I'll take it")
    else:
        print("No way!")
elif place == "space" or place == "Space":
    print("Decision: 'Without a doubt, I'll take it")
else:
    if amount > 6000000:
        print("Sure i can work with that")
    else:
        print("No thanks, I can get something better")