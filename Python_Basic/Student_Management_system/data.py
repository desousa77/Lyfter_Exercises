import csv

def read_data_students_CSV(file_path):
    with open(file_path, encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        student_data = list(reader)
    return student_data    

def main():
    file_input = 'Data_Students.csv'
    print(read_data_students_CSV(file_input))

if __name__ == '__main__':
    main()