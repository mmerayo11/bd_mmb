import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if row[7] == 'AvgTemperature':
        continue

    country = row[1]
    temperature = float(row[7])

    if temperature > -90:
        print(f"{country}\t{temperature}")