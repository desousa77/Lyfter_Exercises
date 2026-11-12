input_file = 'Word_to_counter.txt'
new_input_file = 'Upper_Words_converter.txt'

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def uppercase_converter(file_text):
    upper_text = file_text.upper()
    return upper_text

def write_new_file(file_name, file_content):
    with open(file_name, 'w', encoding='utf-8') as new_file:
        new_file.writelines(file_content)
        print()
        print("The new file was created successfully.!!!")
        print()

def main():
    text_to_converter = read_file(input_file)
    upper_text = uppercase_converter(text_to_converter)
    write_new_file(new_input_file, upper_text)

if __name__ == '__main__':
    main()