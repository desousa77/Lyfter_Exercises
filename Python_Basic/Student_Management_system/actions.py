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

def student_exists(data_student, students):
    
    for student in students:
        if(
        student["full_name"].strip() == data_student["full_name"].strip()
        and
        student["section"].strip() == data_student["section"].strip()
        ):
            return True
    
    return False

def save_student(student_data, students):
    if student_exists(student_data, students):
        print()
        print(f"{RED}This student already exists.")
        return False
    
    students.append(student_data)    
    print()
    print(f"{YELLOW}The student information was saved successfully.")
    print()
    return True
        
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
    
    for student in students:
        if (
            student["full_name"].strip() == data_student["full_name"].strip()
            and
            student["section"].strip() == data_student["section"].strip()
        ):    
            students.remove(student)
            return True        
def show_no_data_message(students):
    if not students:
        print()
        print(f"{YELLOW}No student data available in memory. Please add or import students first.")
        return False
    return True

def delete_student(students):
    if not show_no_data_message(students):
        return
    
    data_student = get_student_to_delete()
    
    if student_exists(data_student, students):
        if confirm_student_deletion():
            remove_student_from_list(students, data_student)
            print(f"{YELLOW}Student successfully deleted.")
        else:
            print()
            print(f"{YELLOW}Student deletion cancelled.")    
    else:
        print()
        print(f"{YELLOW}Student not found.")

def show_all_students(students):
    if not show_no_data_message(students):
        return
    
    print()
    print(f"{CYAN}{BOLD}Student General Report\n")
    for student_data in students:
        print(f"{GREEN}\tStudent Name: {YELLOW}{student_data['full_name']}")
        print(f"{GREEN}\tStudent Section: {YELLOW}{student_data['section']}")
        print(f"{GREEN}\tSpanish Grade: {YELLOW}{student_data['spanish_grade']}")
        print(f"{GREEN}\tEnglish Grade: {YELLOW}{student_data['english_grade']}")
        print(f"{GREEN}\tSocial Studies Grade: {YELLOW}{student_data['social_s_grade']}")
        print(f"{GREEN}\tScience Grade: {YELLOW}{student_data['science_grade']}")
        print(f"{CYAN}---------------------------------------------------------------------------")

def get_top_three_students(students):
    students = calculate_student_average(students)
    top_three = students[:3]
    return top_three

def show_top_three_students(top_list):
    if not show_no_data_message(top_list):
        return
    print()
    print(f"{CYAN}{BOLD}\tTop 3 Students - Highest Average Grades.!!!\n")
    for top_student in top_list:
        print(f"{GREEN}Student Name: {YELLOW}{top_student['full_name']}")
        print(f"{GREEN}Student Section: {YELLOW}{top_student['section']}")
        print(f"{GREEN}Student Average: {YELLOW}{top_student['average']}\n")
        print(f"{CYAN}---------------------------------------------------------------------------")

def calculate_student_average(data_student):
    student_by_avg =[] 
    for student in data_student:
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
    student_by_avg = sorted(
        student_by_avg,
        key=lambda student: student['average'],
        reverse=True
        )
    return student_by_avg

def calculate_group_avg(students_avg):
    if not students_avg:
        return 0
    
    sum_avg = 0

    for student_avg in students_avg:
        sum_avg += student_avg['average']
    group_avg =  sum_avg / len(students_avg)    

    return group_avg    
def show_group_average(group_avg):
    if not show_no_data_message(group_avg):
        return
    
    print()
    print(f"{CYAN}{BOLD}Group Average Grade\n")
    print(f"{GREEN}Overall Group Average: {YELLOW}{group_avg:.2f}")
    print()

def get_failing_students(students):
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
    if not failing_data:
        print()
        print(f"{YELLOW}Congratulations! No students with failing grades")
        return 
    print()
    print(f"{CYAN}{BOLD}\t Students With Failing Grades.!!!\n")
    for student in failing_data:
        print(f"{GREEN}Student Name: {YELLOW}{student['full_name']}")
        print(f"{GREEN}Student Section: {YELLOW}{student['section']}")
        if student['spanish_grade'] < 60:
            print(f"{GREEN}Student Spanish Grade: {RED}{student['spanish_grade']}")
        if student['english_grade'] < 60:    
            print(f"{GREEN}Student English Grade: {RED}{student['english_grade']}")
        if student['social_s_grade'] < 60:    
            print(f"{GREEN}Student Social Studios Grade: {RED}{student['social_s_grade']}")
        if student['science_grade'] < 60:
            print(f"{GREEN}Student Science Grade: {RED}{student['science_grade']}")
        print(f"{GREEN}Student Status: {RED}{student['status']}\n")
        print(f"{CYAN}---------------------------------------------------------------------------")    