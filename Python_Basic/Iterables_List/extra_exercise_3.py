print()
print("Hello, please create a new numbers list!")

while True:
    len_list = int(input("Please enter how many numbers you want in the new list: "))
    if len_list <= 1:
        print("You must enter at least 2 numbers in the list.")
    else:
        break

my_list =[]
smallest_number =0
for index in range (0, len_list):
    number = int(input("Enter the new list number: "))
    my_list.append(number)
    if index== 0:
        smallest_number = number
    if number < smallest_number:
        smallest_number = number
print()
print(my_list)
print(f"The smallest value is: {smallest_number}")
