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

success = {
    "Haidar": 100000,
    "Noor": -30000,
    "Hamdi": -999999,
    "Mahmoud": 930999,
    "Kareem": 910099,
    "Ammar": 902999
}
failure = {
    "Haidar": "  _____________"
              "- |     |     |"
              "  |_____|_____|",
    "Hamdi":   "_____________"
             "+ |     |     |"
               "|_____|_____|",
    "Noor": 9999999,
    "Mahmoud": -900000,
    "Kareem": -900000,
    "Ammar": -900000
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

file_path = "degree_of_success.json"

try:
    with open(file_path, "x") as file:
        json.dump(success, file, indent="\n")
        print(f"Json file {file_path} has been created.")
except FileExistsError:
    file_path = "degree_of_failure.json"
    with open(file_path, "w") as file:
        json.dump(failure, file, indent="\n")
        print(f"Json file {file_path} has been modified.")
