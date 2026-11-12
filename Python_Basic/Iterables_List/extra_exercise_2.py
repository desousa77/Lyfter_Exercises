print()
print("Welcome, please go to create a new list numbers")
print()

while True:
    len_list = int(input("Please enter how many numbers you want in the new list: "))
    if len_list <= 1:
        print("You must enter at least 2 numbers in the list.")
    else:
        break

list_numbers =[]
negative = False
for index in range(0, len_list):
    number = int(input("Enter the number:"))
    list_numbers.append(number)
    if number <=0:
        negative = True
if negative:
    print("There is at least one negative number or zero.")
else:
    print("No number is negative or zero")