import csv

def compare_rows(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='r', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictReader(outfile)
        
        count = 0
        accuracy = 0

        for in_row, out_row in zip(reader, writer):
            if in_row["label"] == out_row["label"]:  # Compare labels
                accuracy += 1
            count += 1
            if count == 500:
                break
        
        # Calculate the accuracy percentage
        if count > 0:
            accuracy_percentage = (accuracy / count) * 100
        else:
            accuracy_percentage = 0
        
        print(f"Accuracy: {accuracy_percentage:.2f}%")

compare_rows("finaloutput.csv", "snorkel-2021-10.csv")
