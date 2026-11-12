input_file = 'Hello_world.txt'
new_input_file = 'New_Hello_World.txt'

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace('\n', ' ')
    return content

def write_new_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as new_file:
        new_file.writelines(text)
        print()
        print("The new file was created successfully")

def main():
    new_text = read_file(input_file)
    write_new_file(new_input_file, new_text)

if __name__ == '__main__':
    main()        
    
