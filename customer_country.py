import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

with open("customer_country.csv", "w", newline="") as file:
    country_file = csv.writer(file, delimiter=",")
    country_file.writerow(["First Name", "Last Name", "Country"])

    for record in customer_file:
        # write to file with first name, last name, country order
        country_file.writerow([record[1], record[2], record[4]])
