from pathlib import Path
import json
import csv
from tqdm import tqdm

# Define the parent directory where the folders are located
parent_directory = Path("E:\Google Takeout\photos-12-23")  

# Use glob to find all JSON files in the specified folders
json_files = parent_directory.glob("**/*.json")

# Open the CSV file for writing
with open("output.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header row
    csv_writer.writerow(["File Name", "Photo Taken Time", "Photo Creation Time"])

    # Iterate through each JSON file and load the data
    for idx, json_file in tqdm(enumerate(json_files)):
        # if idx < 20:
        with open(json_file, 'r', encoding="UTF8") as file:
            print(json_file.name)
            try:
                # Load JSON data
                json_data = json.load(file)
                photo_taken_time = json_data.get("photoTakenTime")
                if photo_taken_time:
                    photo_taken_time = photo_taken_time["formatted"]
                photo_creation_time = json_data.get("creationTime")
                if photo_creation_time:
                    photo_creation_time = photo_creation_time["formatted"]

                # Write row to CSV
                csv_writer.writerow([json_file.name, photo_taken_time, photo_creation_time])
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {json_file}: {e}")
    # else:
    #     break

print(f"CSV file has been created.")