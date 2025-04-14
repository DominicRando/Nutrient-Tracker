import os
import csv

# for the daily_total_intake table, for intake_id, needed to make the values start at 1 and increment
# this script does that 
rows = []
with open('../Data/daily_total_intake.csv', mode = 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        # Example condition: update "recommended_amount" if "nutrient_name" is "Vitamin C"
        row["intake_id"] = i
        rows.append(row)
        i+=1

with open('../Data/daily_total_intake.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
