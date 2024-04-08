import json
import os

json_folder = 'code-challenge-2024-KudoC0nan/mempool'

def import_files(json_folder):
    json_data_list = []
    json_files = os.listdir(json_folder)

    for file_name in json_files:
        file_path = os.path.join(json_folder, file_name)
        
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
            json_data_list.append(json_data)

    return json_data_list

json_data_list = import_files(json_folder)

print(json_data_list[0])