import csv

infile = open("customers.csv", "r")

csvfile = csv.reader(infile, delimiter = ',')

outfile = open("customer_country.csv", 'w')

next(csvfile)

outfile.write("Full Name, Country\n")
#skip the first line which is the header line

for record in csvfile: 
    fullname = record[1] + ' ' + record[2]
    country = record[4]
    outfile.write(fullname + ',' + country + '\n')

outfile.close()