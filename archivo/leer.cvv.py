import csv

with open("archivo\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    for row in reader:
        print(row)