import csv

input_file_path = r'C:\Users\spenc\Downloads\Fully Filtered Tweet Dataset - filtered_output_english.csv'  # The input CSV file path
output_file_path = 'filtered_tweets.csv'  # The output CSV file path

# Read the input CSV file and filter rows
with open(input_file_path, 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    filtered_data = [row for row in reader if row['labeled'] == '1']

# Ensure there is data to write
if not filtered_data:
    print("No entries with 'labeled' = 1 found in the CSV file.")
else:
    # Write the filtered data to the new CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_csv_file:
        writer = csv.DictWriter(output_csv_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in filtered_data:
            writer.writerow(row)

    print("Filtered CSV data has been successfully written to filtered_tweets.csv")
