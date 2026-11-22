import time
from actions import get_data_new_student, save_student_to_csv, ask_for_another_student, show_all_students, get_top_three_students
from actions import show_top_three_students, calculate_student_average, show_students_average, get_failing_students, show_failing_students
from actions import delete_student
from data import get_student_file_path, get_file_name_to_export_import, read_data_students_CSV, write_students_csv, import_file_csv


CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

file_input = get_student_file_path()

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
    print(f"\t{GREEN}| 4. View Student Grades             |")
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
    #print(f"Correct option: {option}")    
    return True

def execute_menu_option(option):
    if option == 1:   
        student_data = get_data_new_student()
        save_student_to_csv(file_input, student_data)
        if not ask_for_another_student():
            print()
            print(f"{GREEN}Student registration completed.")
            print()
            return True
    if option == 2:
        show_all_students(file_input)
        return True
    if option == 3:
        top_three = get_top_three_students(file_input)
        show_top_three_students(top_three)
        return True
    if option == 4:
        students_avg = calculate_student_average(file_input)
        show_students_average(students_avg)
        return True
    if option == 5:
        failing_students = get_failing_students(file_input)
        show_failing_students(failing_students)
        return True
    if option == 6:
        delete_student(file_input)
        print()
        print(f"{YELLOW}Student information deleted successfully.")    
        return True
    if option == 7:
        data_export = read_data_students_CSV(file_input)
        export_file_path = get_file_name_to_export_import()
        write_students_csv(export_file_path, data_export)
        print()
        print(f"{YELLOW}The data was successfully exported! The file {export_file_path} has been created.")
        return True
    if option == 8:
        import_file_path = get_file_name_to_export_import()
        import_file_csv(file_input, import_file_path)
        return True

    
    if option == 9:        
        return False