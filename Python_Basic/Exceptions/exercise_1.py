def main():
    current_number = 0
    while True:
        main_menu(current_number)
        user_choice = get_user_choice()
        if user_choice==7:
            print("Thank you for using the Console Calculator. Goodbye!")
            break        
        if user_choice ==1:            
            user_number = get_user_number()
            current_number = add_numbers(current_number, user_number)
            print(f"The addition result is: {current_number}")
        elif user_choice ==2:
            user_number = get_user_number()
            current_number = subtract_numbers(current_number, user_number)
            print(f"The subtraction result is: {current_number}")
        elif user_choice ==3:
            user_number = get_user_number()
            current_number = multiply_numbers(current_number, user_number)
            print(f"The multiplication result is: {current_number}")
        elif user_choice ==4:
            while True:
                try:
                    user_number = get_user_number()
                    current_number = divide_numbers(current_number, user_number)
                    print(f"The division result is: {current_number}")
                    break
                except ZeroDivisionError as error:
                    print(f"Error: {error} is not allowed. Please enter a non-zero number.")    
        elif user_choice ==5:
            current_number = set_current_number()
            print(f"The new current number value is: {current_number}")            
        elif user_choice ==6:
            current_number = clear_result()
            print(f"The current number has been reset to: {current_number}")      
        
        if ask_to_continue() == "N":
            print("Thank you for using the Console Calculator. Goodbye!")
            break

def main_menu(number):
    print()
    print(
         "\n*** Console Calculator ***\n"
        f"The current number in memory is: {number}\n"
        "*****************************************************\n"
        "Main Menu:\n"
        "Option #1 Addition\n"
        "Option #2 Subtraction\n"
        "Option #3 Multiplication\n"
        "Option #4 Division\n"
        "Option #5 Change Current Number\n"
        "Option #6 Clear Result\n"
        "Option #7 Exit !!!\n"
    )
    
def get_user_choice():
    while True:
        try:
            
            user_choice = int(input("Enter your option (1-7): "))
            
            if 1<= user_choice <=7:
                print("************************************")
                print(f"You picked option #{user_choice}.")
                return user_choice
            print("Invalid option. Please enter a number between 1 and 7")                

        except ValueError as error:
            print(f"Error: {error}, Please enter numbers only.!!!")
            
            

def get_user_number():
    while True:
        try:
            user_number = float(input("Please enter a number to the calculator operation: "))
            return user_number
        except ValueError as error:
            print(f"Error: {error}. Please enter numbers only (Integers or Decimals).!!!")

def add_numbers(current_number, user_number):    
    return current_number + user_number
    

def subtract_numbers(current_number, user_number):
    return current_number - user_number

def multiply_numbers(current_number, user_number):
    return current_number * user_number
    
def divide_numbers(current_number, user_number):
    return current_number / user_number

def set_current_number():    
    while True:
        try:
            current_number = float(input("Please enter the new value for the current number: "))            
            return current_number
        except ValueError as error:
            print(f"Error: {error}. Please enter only numbers for the new current number value.!!!")    

def clear_result():
    current_number = 0
    return current_number

def ask_to_continue():
    while True:
        repeat = input("Do you want to continue using the command-line calculator? Y/N: ").upper()        
        if repeat =='Y' or repeat=='N': 
            return repeat 
        else:
            print("Please enter an option: Y/N to continue..!!")

if __name__ == "__main__":
    main()