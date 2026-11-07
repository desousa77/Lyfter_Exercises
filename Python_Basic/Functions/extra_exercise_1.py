def count_character_in_text(text,string):
    count = 0
    for character in text:
        if string == character:
            count += 1
    return count
user_text = str(input("Enter the text to be checked: "))
user_string= str(input("Enter the character to find into the text: "))
result = count_character_in_text(user_text, user_string)
print()
print(f"The character '{user_string}', was found {result} times..!!")
