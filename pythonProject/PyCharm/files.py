import os
import json
import csv

 # Detection

file_path = "C:/Users/munth/Pictures/Saved Pictures/desktop.ini"

if os.path.exists(file_path):
    print(f"'{file_path}' exists.")
    if os.path.isfile(file_path):
        print("It is a file.")
    else:
        print("It is a directory")
else:
    print("Invalid location.")

# Writing

text_data = "Python writing test."

dir_path = "C:\\Programming\\Python\\pythonProject\\PyCharm"
file_path = "test.txt"

objects = {
    "coffee": "cup",
    "water bottles": 3,
    "TV": "BBC News",
    "Table": "Coffee tray"
}

if os.path.exists(dir_path):
    try:
        with open(file_path, "x") as file:
            file.write(text_data)
            print(f"Text file {file_path} has been created.")
    except FileExistsError:
        with open(file_path, "w") as file:
            file.write("Override complete.")
            print(f"Text file {file_path} has been modified.")

file_path = "objects.json"

try:
    with open(file_path, "x") as file:
        json.dump(objects, file, indent="\n")
        print(f"Json file {file_path} has been created.")
except FileExistsError:
    with open(file_path, "w") as file:
        json.dump(objects, file, indent="\n")
        print(f"Json file {file_path} has been modified.")
