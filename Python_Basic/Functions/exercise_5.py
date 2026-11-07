def count_string(string):
    counter_upper = 0
    counter_lower = 0
    for index in string:
        if index.isupper():
            counter_upper += 1
        elif index.islower():
            counter_lower +=1
    print(f"There's: {counter_upper} upper case and : {counter_lower} lower case")

string_to_count = "I Really Enjoy Programming in Python"
count_string(string_to_count)