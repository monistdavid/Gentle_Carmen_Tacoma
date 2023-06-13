import csv
import json

def merge_csv_json(csv_file, json_file, output_file):
    # Read the CSV file and create a dictionary with dealerId as the key
    csv_data = {}
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            dealer_id = row[0]
            dealer_name = row[2]
            dealer_url = row[3]
            dealer_state = row[5]
            csv_data[dealer_id] = {'dealerName': dealer_name, 'dealerURL': dealer_url, 'state': dealer_state}

    # Read the JSON file and merge lines with the same dealerId
    merged_data = []
    with open(json_file, 'r') as jsonfile:
        json_data = json.load(jsonfile)
        for item in json_data:
            dealer_id = item['dealer']
            if dealer_id in csv_data:
                merged_item = {**item, **csv_data[dealer_id]}
                merged_data.append(merged_item)

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=2)

# Usage
csv_file = 'dealers.csv'
json_file = 'inventory.json'
output_file = 'merged_data.json'

merge_csv_json(csv_file, json_file, output_file)
