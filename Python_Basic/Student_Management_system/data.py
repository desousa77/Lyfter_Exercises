import csv
YELLOW = "\033[93m"

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
    print()
    print(f"{YELLOW}Student information deleted successfully.")    