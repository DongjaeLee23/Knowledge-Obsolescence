import json
import csv

# Load JSON data
data = []
with open(r'C:\Users\spenc\Downloads\tweets-2021-10-01-extended.json\tweets-2021-10-01-extended.json', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

# Define fieldnames for the CSV, including the new 'labeled' field
fieldnames = ["full_text", "labeled"]

# Write to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in data:
        full_text = tweet.get("full_text", "")
        if full_text[:2] != "RT":
            writer.writerow({"full_text": full_text, "labeled": 0})

print("Filtered JSON data with 'labeled' field has been successfully written to output.csv")
