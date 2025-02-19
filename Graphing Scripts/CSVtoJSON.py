import csv
import json

csvfile = open('2021-10-01.csv', 'r', encoding='utf-8')
jsonfile = open('2021-10-01.json', 'w', encoding='utf-8')

fieldnames = ("text","label")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

csvfile.close()
jsonfile.close()