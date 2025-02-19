import csv
from langdetect import detect, LangDetectException

input_file_path = r'C:\Users\spenc\Downloads\labeled_tweets - output.csv'  # The input CSV file path
output_file_path = 'filtered_output_english.csv'  # The output CSV file path

# Function to check if the text is in English
def is_english(text):
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

# Read the input CSV file and filter rows
with open(input_file_path, 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    filtered_data = [row for row in reader if is_english(row['full_text'])]

# Ensure there is data to write
if not filtered_data:
    print("No English entries found in the CSV file.")
else:
    # Write the filtered data to the new CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_csv_file:
        writer = csv.DictWriter(output_csv_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in filtered_data:
            writer.writerow(row)

    print("Filtered CSV data with English entries has been successfully written to filtered_output_english.csv")