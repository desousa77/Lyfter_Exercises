numbers_list = []
print("Please enter 10 numbers.!")
for index in range(1,11):
    number = int(input(f"Enter the number #{index}: "))
    if index ==1:
        largest_number = number        
    if number > largest_number:
        largest_number = number
    numbers_list.append(number)
print("The numbers entered were: ")
print(numbers_list)
print(f"The largest number is: {largest_number} ")