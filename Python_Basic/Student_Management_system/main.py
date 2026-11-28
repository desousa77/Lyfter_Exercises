from menu import get_menu_option, is_valid_menu_option, execute_menu_option, menu
GREEN = "\033[92m"

def main():
    menu()
    students =[]
    while True:
        user_menu = get_menu_option()
        if is_valid_menu_option(user_menu):
            should_continue = execute_menu_option(user_menu, students)
            if not should_continue:
                print()
                print(f"{GREEN}Thank you for using Student Management System. Goodbye!\n")
                break
            else:
                menu()

if __name__ == '__main__':
    main()