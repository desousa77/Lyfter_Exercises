import time
CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def display_title():
    title = "***** STUDENT MANAGEMENT SYSTEM *****"
    print()
    for character in title:
        print(f"{CYAN}{BOLD}{character}", end="", flush=True)
        time.sleep(0.06)

def menu():
    print()
    print(f"\t{GREEN}1. Register New Student")
    print(f"\t{GREEN}2. Student Report")
    print(f"\t{GREEN}3. Top 3 Student By Average Grades") 
    print(f"\t{GREEN}4. View Student Grades")
    print(f"\t{GREEN}5. View Failing Students")
    print(f"\t{YELLOW}6. DELETE Student")
    print(f"\t{YELLOW}7. Export Data To CSV file")
    print(f"\t{YELLOW}8. Import Data From CSV File")
    print(f"\t{RED}9. Exit\n")

display_title()
menu()

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

while True:        
    user_menu = get_menu_option()
    if is_valid_menu_option(user_menu):
        break