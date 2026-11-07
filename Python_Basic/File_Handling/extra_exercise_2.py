input_file = 'Word_to_counter.txt'

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    return text    

def counter_words(text_to_counter):
    words_count = len(text_to_counter.split())
    return words_count

def show_results(words):
    print()
    print(f"The text read contains {words} words.!")
    print()

def main():
    file_text = read_file(input_file)
    count_result = counter_words(file_text)
    show_results(count_result)

if __name__ == '__main__':
    main()