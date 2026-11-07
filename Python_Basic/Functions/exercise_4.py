def reverse_string(string):
    reversed_string =""
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string

word = input("Enter the word to reverse: ")
result = reverse_string(word)
print(f"The Reverse result is: {result}")