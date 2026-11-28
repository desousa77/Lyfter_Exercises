import time
from actions import get_data_new_student, save_student,  ask_for_another_student, show_all_students, get_top_three_students
from actions import show_top_three_students, calculate_student_average, get_failing_students, show_failing_students
from actions import delete_student, calculate_group_avg, show_group_average
from data import get_student_file_path, get_file_name_to_export_import, read_data_students_CSV, write_students_csv, import_file_csv


CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def display_title():
    title = "***** STUDENT MANAGEMENT SYSTEM. *****"
    print()
    for character in title:
        print(f"{CYAN}{BOLD}{character}", end="", flush=True)
        time.sleep(0.05)

def menu():
    display_title()
    print()
    print(f"\t{GREEN}| 1. Register New Student            |")
    print(f"\t{GREEN}| 2. Student Report                  |")
    print(f"\t{GREEN}| 3. Top 3 Student By Average Grades |") 
    print(f"\t{GREEN}| 4. Group Average Grades            |")
    print(f"\t{GREEN}| 5. View Failing Students           |")
    print(f"\t{YELLOW}| 6. DELETE Student                  |")
    print(f"\t{YELLOW}| 7. Export Data To CSV file         |")
    print(f"\t{YELLOW}| 8. Import Data From CSV File       |")
    print(f"\t{RED}| 9. Exit                            |\n")

def get_menu_option():
    print()
    while True:
        try:
            user_option = int(input(f"{CYAN}Please select an option (1-9): "))
            return user_option
        except ValueError:
            print(f"{RED} Invalid input. Please enter a number between 1 and 9.")    

def is_valid_menu_option(option):
    menu_list = [1,2,3,4,5,6,7,8,9]
    if option not in menu_list:
        print(f"{RED}Invalid option. Please select a number between 1 and 9.")
        return False
    return True

def execute_menu_option(option, students):
    if option == 1:   
        while True:
            student_data = get_data_new_student()
            save_student(student_data, students)
            if not ask_for_another_student():
                print()
                print(f"{GREEN}Student registration completed.")
                print()
                return True
    if option == 2:
        show_all_students(students)
        return True
    if option == 3:
        top_three = get_top_three_students(students)
        show_top_three_students(top_three)
        return True
    if option == 4:
        students_avg = calculate_student_average(students)
        group_avg = calculate_group_avg(students_avg)
        show_group_average(group_avg, students)
        return True
    if option == 5:
        failing_students = get_failing_students(students)
        show_failing_students(failing_students)
        return True
    if option == 6:
        delete_student(students)    
        return True
    if option == 7:
        
        if not students:
            print()
            print(f"{YELLOW}No students available in memory. Cannot export data.")
            return True
        
        export_file_path = get_student_file_path()
        write_students_csv(export_file_path, students)
        print()
        print(f"{YELLOW}The data was successfully exported! The file {export_file_path} has been created.")
        return True
    
    if option == 8:
        print()
        print(f"{YELLOW}Please enter the following information to import your data from a CSV file")
        import_file_path = get_student_file_path()
        import_file_csv(students, import_file_path)
        return True

    
    if option == 9:        
        return False