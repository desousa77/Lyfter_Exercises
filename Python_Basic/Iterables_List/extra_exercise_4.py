print()
print("Welcome, please create a new numbers list!")
print()
while True:
    len_list = int(input("Please enter how many numbers you want in the new list: "))
    if len_list <= 1:
        print("You must enter at least 2 numbers in the list.")
    else:
        break
list1 = []
list2 = []
for index in range(0, len_list):
    number = int(input("Please, enter a number to the list: "))
    list1.append(number)
average = sum(list1) / len(list1)
for index in range(0, len_list):
    if list1[index] > average:
        list2.append(list1[index])
print()
print(f"The average is: {average} ")
print(f"The new list is: {list2}")            