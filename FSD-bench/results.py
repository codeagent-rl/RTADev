import csv
from collections import defaultdict

def count_passed_by_category(csv_file_path):
    """
    Reads a CSV file and calculates the total 'passed' count for each category.

    Args:
        csv_file_path (str): Path to the CSV file.

    Returns:
        dict: A dictionary with category as keys and passed totals as values.
    """
    category_passed_count = defaultdict(int)

    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Process each row
        for row in reader:
            category = row['category']
            passed = int(row['passed'])
            category_passed_count[category] += passed

    return category_passed_count

if __name__ == "__main__":
    # Replace with the actual path to your CSV file
    csv_file_paths = ['./RTADev_new60_result.csv']
    totals = {"website":350, "game":309, "gui":223} 
    for csv_file_path in csv_file_paths:
        # Count passed totals by category
        print(csv_file_path)
        result = count_passed_by_category(csv_file_path)
        # Print the results
        print("Passed totals by category:")
        for category, passed_total in result.items():
            print(f"{category}: {passed_total}; Pass Percent: {passed_total/totals[str(category)]}")
          