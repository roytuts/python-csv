import csv

csv1_header = []
csv1_data = []

csv2_header = []
csv2_data = []

with open('csv1.csv') as csv1:
    reader = csv.reader(csv1)
    csv1_header = next(reader, None)

with open('csv2.csv') as csv2:
    reader = csv.reader(csv2)
    csv2_header = next(reader, None)

#print(csv1_header)
#print(csv2_header)

set_1 = set(csv1_header)
set_2 = set(csv2_header)

list_2_items_not_in_list_1 = list(set_2 - set_1)
csv_header = list(csv1_header) + list_2_items_not_in_list_1

#print(csv_header)

with open('csv.csv', 'w') as csvfile:
    fieldnames = csv_header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    with open('csv1.csv') as csv1:
        reader = csv.DictReader(csv1)
        for row in reader:
            #writer.writerow({'NAME': row['NAME'], 'MIDDLENAME': row['MIDDLENAME'], 'SURNAME': row['SURNAME'], 'AGE': row['AGE']})
            writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]], fieldnames[2]: row[fieldnames[2]], fieldnames[3]: row[fieldnames[3]]})
			
    with open('csv2.csv') as csv2:
        reader = csv.DictReader(csv2)
        for row in reader: 
            #writer.writerow({'NAME': row['NAME'], 'MIDDLENAME': row['MIDDLENAME'], 'SURNAME': row['SURNAME'], 'AGE': row['AGE'], 'EMAIL': row['EMAIL']})
            writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]], fieldnames[2]: row[fieldnames[2]], fieldnames[3]: row[fieldnames[3]], fieldnames[4]: row[fieldnames[4]]})