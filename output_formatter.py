import json
import csv

def save_as_json(data, output_file):
    """Save data as a JSON file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving as JSON: {e}")

def save_as_csv(data, output_file):
    """Save data as a CSV file."""
    try:
        # Assuming data is a dictionary
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data.keys())  # Write header
            writer.writerow(data.values())  # Write values
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving as CSV: {e}")
