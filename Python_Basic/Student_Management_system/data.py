import csv, re
from pathlib import Path

YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"

def get_student_file_path():
    base_path = Path(__file__).resolve().parent
    file_path = base_path / get_file_name_to_export_import()
    return file_path

def read_data_students_CSV(file_path):
    with open(file_path, encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        student_data = list(reader)
    return student_data 

def write_students_csv(file_path, students):
    headers = [
        "full_name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_s_grade",
        "science_grade"
    ]
    with open(file_path, 'w', encoding='utf-8', newline='') as file_csv:
        write = csv.DictWriter(file_csv, fieldnames=headers)
        write.writeheader()
        write.writerows(students)
    
def get_file_name_to_export_import():
    while True:
        print()
        user_file_name = input(f"{GREEN}Please enter the file name. Do not use spaces or specials characters: ").strip()
        if is_valid_file_name(user_file_name):
            return user_file_name + ".csv"
        print(f"{RED}Invalid file name. Use only letters, numbers, hyphens (-), and underscores (_).")
        

def is_valid_file_name(file_name):
    return bool(re.fullmatch(r"[a-zA-Z0-9_-]+", file_name))

def file_exists(import_file_path):
    return Path(import_file_path).exists()

def import_file_csv(students, import_file_path):
    if file_exists(import_file_path):
        data_import = read_data_students_CSV(import_file_path)
        
        if not data_import:
            print(f"{YELLOW}The import file is empty. No data was imported.")
            return
        
        students.clear()
        students.extend(data_import)
        
        print()
        print(f"{GREEN}Student data was successfully imported into memory.")
    else:
        print()
        print(f"{YELLOW}The file was not found. Please make sure the file exists and try again.")    