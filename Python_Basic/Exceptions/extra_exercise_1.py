def user_name_information():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("The name cannot contain numbers.")
            return name
            
        except ValueError as error:
            print(f"Error: {error}")

def user_age_information():
    while True:
        try:
            age = int(input("Please enter your age: "))
            return age
            
        except ValueError as error:
            print(f"Error: {error}, The age cannot contain letters.!!")        

def show_information(name, age):  
    print("---------------------------------------")
    print(f"Hello {name}, you age is: {age}")
    print("---------------------------------------")

def main():
    show_information(user_name_information(), user_age_information())

if __name__ == "__main__":
    main()