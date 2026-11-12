def count_vowels(text):
    count = 0
    vowels=['a','e','i','o','u']
    for letter in text:
        if letter in vowels:
            count += 1
    return count
print()
user_text = input("Enter the text to find vowels: ")
result = count_vowels(user_text)
print()
if result==1:
    print(f"The number of vowels in the text is: {result}")
else:
    print(f"The number of vowels in the text are: {result}")
    