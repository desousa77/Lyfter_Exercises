def filter_words_by_length(word_list, parameter_number):
    new_word_list=[]
    for words in word_list:
        if len(words)>parameter_number:
            new_word_list.append(words) 
    return new_word_list

user_words_list =[]
print()
num_words = int(input("Enter the numbers of words to enter: "))
for index in range(0,num_words):
    index_show= index+1
    word_to_list=input(f"Enter the word #{index_show},: ")
    user_words_list.append(word_to_list)
word_length = int(input("Enter the minimum word length: ")) 
result = filter_words_by_length(user_words_list, word_length)

print()
print(f"The new list is: {result}")