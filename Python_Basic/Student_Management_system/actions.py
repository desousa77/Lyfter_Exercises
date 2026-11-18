CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
import csv
import re

def validate_grade(subject):
    while True:
        try:
            grade = float(input(f"{GREEN}\t{subject} Grade: {YELLOW}"))
            if 0<= grade <=100:
                return grade  
            print(f"{RED}Grade must be between 0 and 100.")
        except ValueError:
            print(f"{RED}Input Error. Please enter a valid number.") 

def is_valid_name():
    while True:
        full_name = input(f"{GREEN}\tStudent full name: {YELLOW}").strip().upper()
        for character in full_name:
            if character.isdigit():
                print(f"{RED}Full Name cannot contain numbers.")
                break
        else:    
            return full_name 

def is_valid_section():
    while True:
        section = input(f"{GREEN}\tStudent section: {YELLOW}").strip().upper()               
        if not re.fullmatch(r"\d{2}[A-Z]", section):
            print(f"{RED} Invalid section format. Example: 11A")
            continue
        return section


def get_data_new_student():
    print()
    print(f"{CYAN}{BOLD}Please Enter The Following Student Information.")
    full_name = is_valid_name()
    section = is_valid_section()    
    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English")
    social_s_grade = validate_grade("Social Studies")
    science_grade = validate_grade("Science")

    student_data ={
        "full_name": full_name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_s_grade": social_s_grade,
        "Science_grade": science_grade
    }
    return student_data

def student_exists(file_path, data_student):
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file_csv:
            reader = csv.DictReader(file_csv)

            for student in reader:
                if(
                    student["full_name"].strip() == data_student["full_name"].strip()
                    and
                    student["section"].strip() == data_student["section"].strip()
                ):
                    return True
    except FileNotFoundError:
        return False            
    return False

def save_student_to_csv(file_path, data_student):
    
    if student_exists(file_path, data_student):
        print()
        print(f"{RED}Student | {data_student["full_name"]}, section: {data_student["section"]} | already exists.")
        return False
    
    with open(file_path, 'a', encoding='utf-8', newline='') as file_csv:
        headers = data_student.keys()
        write = csv.DictWriter(file_csv, fieldnames=headers)
        
        if file_csv.tell() == 0:
            write.writeheader()
        
        write.writerow(data_student)
        
        print()
        print(f"{YELLOW}The student information was saved successfully.")
        print()
        
def ask_for_another_student():
    while True:
        answer = input(f"{CYAN}\nDo you want to add another student? (y/n): ").lower().strip()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print(f"{RED}Invalid option. Please enter 'y' or 'n'")    

def get_student_to_delete():
    print()
    print(f"{YELLOW}Please enter the following student information to DELETE.")
    full_name = is_valid_name()
    section = is_valid_section()
    
    student_data_to_delete ={
        "full_name": full_name,
        "section": section
    }
    return student_data_to_delete

def confirm_student_deletion():
    print()
    while True:
        if student_exists:
            answer = input(f"{YELLOW}Are you sure you want to delete this student?: ").lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print(f"{RED}Invalid option. Please enter 'y' or 'n'")

def main():
    file_input = 'Data_Students.csv'
    while True:
        student_data = get_data_new_student()
        save_student_to_csv(file_input, student_data)

        if not ask_for_another_student():
            print()
            print(f"{GREEN}Student registration completed.")
            print()
            break

if __name__ == '__main__':
    main()            