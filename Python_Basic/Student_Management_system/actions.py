CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
import csv
import re
from data import read_data_students_CSV, write_students_csv

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
        "science_grade": science_grade
    }
    return student_data

def student_exists(file_path, data_student):
    students = read_data_students_CSV(file_path)
    
    for student in students:
        if(
        student["full_name"].strip() == data_student["full_name"].strip()
        and
        student["section"].strip() == data_student["section"].strip()
        ):
            return True
    
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
            answer = input(f"{RED}Are you sure you want to DELETE this student? (y/n): ").lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print(f"{RED}Invalid option. Please enter 'y' or 'n'")

def remove_student_from_list(students, data_student):
    new_students = []

    for student in students:
        if not (
            student["full_name"].strip() == data_student["full_name"].strip()
            and
            student["section"].strip() == data_student["section"].strip()
        ):    
            new_students.append(student)
    return new_students

def delete_student(file_path):
    data_student = get_student_to_delete()
    students = read_data_students_CSV(file_path)

    if student_exists(file_path, data_student):
        if confirm_student_deletion():
            students = remove_student_from_list(students, data_student)
            write_students_csv(file_path, students)
        else:
            print()
            print(f"{YELLOW}Student deletion cancelled.")    
    else:
        print()
        print(f"{YELLOW}Student not found.")

def show_all_students(file_path):
    data_students = read_data_students_CSV(file_path)
    print()
    print(f"{CYAN}{BOLD}Student General Report\n")
    for students in data_students:
        print(f"{GREEN}\tStudent Name: {YELLOW}{students['full_name']}")
        print(f"{GREEN}\tStudent Section: {YELLOW}{students['section']}")
        print(f"{GREEN}\tSpanish Grade: {YELLOW}{students['spanish_grade']}")
        print(f"{GREEN}\tEnglish Grade: {YELLOW}{students['english_grade']}")
        print(f"{GREEN}\tSocial Studies Grade: {YELLOW}{students['social_s_grade']}")
        print(f"{GREEN}\tScience Grande: {YELLOW}{students['science_grade']}")
        print(f"{CYAN}---------------------------------------------------------------------------")

def get_top_three_students(file_path):
    student_avg = calculate_student_average(file_path)
    
    student_avg.sort(
        key=lambda student: student['average'],
        reverse=True
    )
    top_three = student_avg[:3]
    return top_three

def show_top_three_students(top_list):
    print()
    print(f"{CYAN}{BOLD}\tTop 3 Students - Highest Average Grades.!!!\n")
    for top_students in top_list:
        print(f"{GREEN}Student Name: {YELLOW}{top_students['full_name']}")
        print(f"{GREEN}Student Section: {YELLOW}{top_students['section']}")
        print(f"{GREEN}Student Average: {YELLOW}{top_students['average']}\n")
        print(f"{CYAN}---------------------------------------------------------------------------")

def calculate_student_average(file_path):
    data_students = read_data_students_CSV(file_path)
    student_by_avg =[] 
    for student in data_students:
        name = student['full_name']
        section = student['section']
        avg = (
            float(student['spanish_grade']) + 
            float(student['english_grade']) + 
            float(student['social_s_grade']) + 
            float(student['science_grade']) 
        ) / 4
        student_by_avg.append({
            "full_name": name,
            "section": section,
            "average": avg
        })
    student_by_avg.sort(
        key=lambda student: student['average'],
        reverse=True
    )
    return student_by_avg

def show_students_average(students_list):
    print()
    print(f"{CYAN}{BOLD}\t Students Ranked by Average Grade.!!!\n")
    for students in students_list:
        print(f"{GREEN}Student Name: {YELLOW}{students['full_name']}")
        print(f"{GREEN}Student Section: {YELLOW}{students['section']}")
        print(f"{GREEN}Student Average: {YELLOW}{students['average']}\n")
        print(f"{CYAN}---------------------------------------------------------------------------")    

def get_failing_students(file_path):
    students = read_data_students_CSV(file_path)
    students_failing = []
    for student in students:
        name = student['full_name']
        section = student['section']
        grades = [
            float(student['spanish_grade']),
            float(student['english_grade']),
            float(student['social_s_grade']),
            float(student['science_grade'])
        ]
        if any(grade < 60 for grade in grades):
            students_failing.append({
                "full_name": name,
                "section": section,
                "spanish_grade": grades[0],
                "english_grade": grades[1],
                "social_s_grade": grades[2],
                "science_grade": grades[3],
                "status": "Failing"

            })
    return students_failing

def show_failing_students(failing_data):
    print()
    print(f"{CYAN}{BOLD}\t Students With Failing Grades.!!!\n")
    for student in failing_data:
        print(f"{GREEN}Student Name: {YELLOW}{student['full_name']}")
        print(f"{GREEN}Student Section: {YELLOW}{student['section']}")
        print(f"{GREEN}Student Spanish Grade: {YELLOW}{student['spanish_grade']}")
        print(f"{GREEN}Student English Grade: {YELLOW}{student['english_grade']}")
        print(f"{GREEN}Student Social Studios Grade: {YELLOW}{student['social_s_grade']}")
        print(f"{GREEN}Student Science Grade: {YELLOW}{student['science_grade']}")
        print(f"{GREEN}Student Status: {RED}{student['status']}\n")
        print(f"{CYAN}---------------------------------------------------------------------------")    


