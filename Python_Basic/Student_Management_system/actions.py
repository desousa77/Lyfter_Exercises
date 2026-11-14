CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def validate_grade(subject):
    while True:
        try:
            grade = float(input(f"{GREEN}\t{subject} Grade: {YELLOW}"))
            if 0<= grade <=100:
                return grade  
            print(f"{RED}Grade must be between 0 and 100.")
        except ValueError:
            print(f"{RED}Input Error. Please enter a valid number.")     

def get_data_new_student():
    print()
    print(f"{CYAN}{BOLD}Please Enter The Following Student Information.")
    full_name = input(f"{GREEN}\tStudent full name: {YELLOW}")
    section = input(f"{GREEN}\tStudent section: {YELLOW}")    
    
    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English")
    social_s_grade = validate_grade("Social Studies")
    Science_grade = validate_grade("Science")

    student_data ={
        "full_name": full_name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_s_grade": social_s_grade,
        "Science_grade": Science_grade
    }
    return student_data

print(get_data_new_student())