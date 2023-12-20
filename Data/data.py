import csv

def print_unique_values(file_path):
    unique_values = set()

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the second column (index 1) contains the data you want
            if len(row) > 1:
                unique_values.add(row[1])

    print("Unique values in the second column:")
    for value in unique_values:
        print(value)

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'data-1.csv'
print_unique_values(file_path)