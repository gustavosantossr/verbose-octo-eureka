import csv

# Replace 'your_file.csv' with the path to your actual CSV file
file_path = 'your_file.csv'

# Open the CSV file and read its contents
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # Skip the header if your CSV has one
    next(csv_reader, None)

    # Iterate over each row in the CSV
    for row in csv_reader:
        print(row)  # Each row is a list of values