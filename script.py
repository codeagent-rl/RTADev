import os
import re

def extract_cost_from_log(file_path):
    """
    Extract the cost value from a log.log file.
    :param file_path: Path to the log.log file
    :return: The extracted cost as a float, or None if not found
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Regular expression to match "ALL COST FOR PROJECT IS: $Number"
            match = re.search(r"ALL COST FOR PROJECT IS: (\d+(\.\d+)?)", content)
            if match:
                return float(match.group(1))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def calculate_average_cost(project_path):
    """
    Calculate the average cost across all project_name folders.
    :param project_path: Path to the root /project folder
    :return: Average cost and total cost
    """
    total_cost = 0
    project_count = 0

    for category in os.listdir(project_path):
        category_path = os.path.join(project_path, category)

        if os.path.isdir(category_path):  # Ensure it's a directory
            for project_name in os.listdir(category_path):
                project_path = os.path.join(category_path, project_name)

                if os.path.isdir(project_path):  # Ensure it's a project folder
                    log_file = os.path.join(project_path, 'log.log')

                    if os.path.isfile(log_file):
                        cost = extract_cost_from_log(log_file)
                        if cost is not None:
                            total_cost += cost
                            project_count += 1

    # Calculate average cost
    average_cost = total_cost / project_count if project_count > 0 else 0
    return total_cost, average_cost

def main():
    # Define the root project directory
    root_project_path = './project-woRTA'
    
    # Calculate total and average cost
    total, average = calculate_average_cost(root_project_path)
    
    # Output results
    print(f"Total Cost: ${total:.2f}")
    print(f"Average Cost per Project: ${average:.2f}")

if __name__ == "__main__":
    main()