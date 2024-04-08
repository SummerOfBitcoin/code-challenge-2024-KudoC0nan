import json
import os

# List all files in the directory
def import_files(json_folder):
    json_data_list = []
    json_files = os.listdir(json_folder)

    # Iterate over each JSON file
    for file_name in json_files:
        # Construct the full path to the JSON file
        file_path = os.path.join(json_folder, file_name)
        
        # Open and load the JSON file
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
            json_data_list.append(json_data)

    return json_data_list