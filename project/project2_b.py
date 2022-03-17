def open_file():
    while True:
        # Prompting the user for name of input file
        file = input("Enter the name of the file: ")
        #If the user enters a valid file name, the program will execute in the try block
        #If the user enters an invalid file name, the program will execute in the except block
        try:
            with open(file) as inputfile:
                return file
        except:
            print("Unable to locate file")
            continue

def process_file(file_to_use):
    # Prompting the user for a year and income level
    year = input("Enter a year: ")
    # Guiding the user on the accepted income level inputs needed
    print("Please not the following income levels and their translations\n\t'1' - low income\n\t'2' - lower middle income\n\t'3' - upper middle income\n\t'4' - high income")
    income_level = input("Enter an income level: ")
    with open(file_to_use) as opened_file:
#Initializing different variables to ease the creation of the summary report
        count = 0
        count1 = 0
        minimum_percentage = 100
        country_highest = ""
        country_lowest = ""
        maximum_percentage = 0
        total = 0
# Iterating line per line looking for specific income status
#For every iteration we want to add the count 1 in order to know how many entries are present in the file
#Still for every iteration, we add 1 to count for a specific income status to find out how many entries are present with the desired income status
#Similarly you can use count1 = len(opened_file.readlines()) to achieve the same result. In that case you dont have to add 1 to count1 every iteration of the loop
        for line in opened_file:
            count1 += 1
            if income_level == "1":
                if line[88:].startswith(year):
                    if "WB_LI" in line:
                        total += 1
                        count += int(line[59:62])
            elif income_level == "2":
                if line[88:].startswith(year):
                    if "WB_LMI" in line:
                        total += 1
                        count += int(line[59:62])
            elif income_level == "3":
                if line[88:].startswith(year):
                    if "WB_UMI" in line:
                        total += 1
                        count += int(line[59:62])
            elif income_level == "4":
                if line[88:].startswith(year):
                    if "WB_HI" in line:
                        total += 1
                        count += int(line[59:62])
            else:
                print("Income level not found")
#Next we assign the proper values that are required checking every entry for the maximum percent and country with that record
            if int(line[59:62]) < minimum_percentage:
                if int(line[88:]) == int(year):
                    minimum_percentage = int(line[59:62])

            if int(line[59:62]) > maximum_percentage:
                if int(line[88:]) == int(year):
                    maximum_percentage = int(line[59:62])

    number_of_countries_with_highest = 0
    number_of_countries_with_lowest = 0

    with open(file_to_use) as new:
        for line in new:
            if line[88:].startswith(year):
                if int(line[59:62]) == maximum_percentage:
                    number_of_countries_with_highest += 1
                    country_highest += "\n" + line[:51]

            if line[88:].startswith(year):
                if int(line[59:62]) == minimum_percentage:
                    number_of_countries_with_lowest += 1
                    country_lowest += "\n" + line[:51]
#Outputting the summary report
    print()
    print("_" * 50)
    print(">" * 50)
    print("SUMMARY REPORT")
    print(">" * 50)
    print("_" * 50)
    print()
    print(f"Count in income status specified: {total}\n")
    print(f"Average percentage of records: {round((count / total) ,2)}\n")
    if number_of_countries_with_lowest > 1:
        print(f"Countries with the lowest percentage for {year} and income level {income_level}: {country_lowest} \nwith a percentage of: {minimum_percentage}\n")
    else:
        print(f"Country with the lowest percentage for {year} and income level {income_level}: {country_lowest} \nwith a percentage of: {minimum_percentage}\n")
    if number_of_countries_with_highest > 1:
        print(f"Countries with the highest percentage for {year} and income level: {income_level}: {country_highest} \nwith a percentage of: {maximum_percentage}")
    else:
        print(f"Country with the highest percentage for {year} and income level: {income_level}: {country_highest} \nwith a percentage of: {maximum_percentage}")

def main():
    file_to_be_used = open_file()
    process_file(file_to_be_used)

main()