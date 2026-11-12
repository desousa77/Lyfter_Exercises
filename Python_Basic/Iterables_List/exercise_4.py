my_list = [1,2,3,4,5,6,7,8,9]
for index in range(len(my_list) -1, -1, -1):
    number = my_list[index]
    if number % 2 !=0:
        my_list.pop(index)
print(my_list)
