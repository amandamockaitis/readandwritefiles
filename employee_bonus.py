import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

next(employee_file)

for record in employee_file:

    # put in individual lines to make it readable
    print("ID:", record[0])
    # full name printed as first last
    print("Full Name:", record[1], record[2])
    print("Salary:", record[3])
    print("Bonus:", record[4])
    # put in line to make it readable
    print("---------------------")
