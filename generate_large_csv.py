import csv
import sys

def generate_large_csv(file_path, num_rows):
    header = ["Name", "Age", "City"]

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header
        writer.writerow(header)
        
        # Write sample data
        for i in range(1, num_rows + 1):
            writer.writerow(["John Doe", i, "New York"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_large_csv.py <output_file_path> <num_rows>")
        sys.exit(1)

    output_file_path = sys.argv[1]
    num_rows = int(sys.argv[2])

    generate_large_csv(output_file_path, num_rows)
    print(f"CSV file generated: {output_file_path}")
