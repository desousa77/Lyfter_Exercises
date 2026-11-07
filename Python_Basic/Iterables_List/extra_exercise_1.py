numbers_list = []
while True:
    number = int(input("Enter a number: "))
    numbers_list.append(number)
    answer = input("Do you want to enter an other number? (y/n): ")
    if answer =="n":        
        break
number_to_find = int(input("Enter the number to find: "))
counter = 0
for index in range(0, len(numbers_list)):
    if number_to_find == numbers_list[index]:
        counter = counter + 1
print("\n")
print(f"Numbers entered: {numbers_list}")
if counter > 0:
    print(f"The number: {number_to_find}, appears {counter} times.")
else:
    print(f"The number {number_to_find}, does not appear in the list of numbers")    