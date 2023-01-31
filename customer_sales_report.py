# program that reads the sales.csv file
# creates a new file with the customer ID and calculated total (as shown in salesreport.csv)
import csv

with open("sales.csv", "r") as sales_file:
    sales = csv.reader(sales_file)
    next(sales)
    calculated_total = {}
    for row in sales:
        customer_id = row[0]
        amount1 = float(row[3])
        amount2 = float(row[4])
        amount3 = float(row[5])
        total = amount1 + amount2 + amount3

        if customer_id in calculated_total:
            calculated_total[customer_id] += total
        else:
            calculated_total[customer_id] = total

with open("salesreport.csv", "w", newline="") as salesreport_file:
    salesreport = csv.writer(salesreport_file)
    salesreport.writerow(["Customer ID", "Total"])
    for customer_id, total in calculated_total.items():
        salesreport.writerow([customer_id, total])
