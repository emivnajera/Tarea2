import csv

with open ('cursos.csv') as data:
    info = csv.reader(data)

    for i in info:
        print(i)