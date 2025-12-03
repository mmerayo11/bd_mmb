import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if row[7] == 'AvgTemperature':
        continue

    city = row[3]
    temperature = float(row[7])
    year = row[6]

    if temperature > -90:
        print(f"{city}\t{year}\t{temperature}")