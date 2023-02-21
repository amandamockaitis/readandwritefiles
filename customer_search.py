import csv

infile = open("customers.csv", "r")

csvfile = csv.reader(infile, delimiter = ',')

searchname = input("Enter the name you want to search for: ")
foundFlag = False
next(csvfile)

for record in csvfile: 
    if record[1].lower() == searchname.lower(): 
        print("Match Found")
        print()
        print(f"First Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"City: {record[3]}")
        print(f"Country: {record[4]}")
        print(f"Phone: {record[5]}")
        foundFlag = True 

if not foundFlag:
    print("match not found")