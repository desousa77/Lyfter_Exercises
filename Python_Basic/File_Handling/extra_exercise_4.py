input_file = 'append_text.txt'

def get_user_input():
    user_input = input("Please, enter the text you want to append to the file: ")
    return user_input

def write_file(file_name, text):
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            file.writelines(text)
            print()
            print("A new file was created with the text entered.!!!")
    except FileExistsError:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.writelines('\n' + text)
            print()
            print("The file already exist. The new text was appended to the las line of the file.!!!")       

def main():
    user_input = get_user_input()
    write_file(input_file, user_input)

if __name__ == '__main__':
    main()