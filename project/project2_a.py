try:
    measles = open("measles.txt", "r")
except:
    quit("Unable to open measles.txt. Try troubleshooting the problem. Sorry for the inconveniences caused!")

output_file = input("Enter output file name: ")
new_file = open(output_file, "w")

year = input("Enter yr: ").lower()
if len(year) <= 4 and len(year) >= 0:
    try:
        if year == "" or year == "all" or int(year):
            for line in measles:
                if year == "" or year == line[88:89] or year == line[88:90] or year == line[88:91] or year == line[88:93] or year == "all":
                    new_file.write(line)
    except:
        quit("invalid year")

measles.close()


