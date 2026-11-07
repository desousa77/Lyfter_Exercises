print()
print("Hello, please create a list with 5 words")
print()
list1=[]
list2=[]
for index in range(0, 5):
    word= input("Enter the word to the list: ")
    list1.append(word)
    if len(word) > 4:
        list2.append(list1[index])
print(f"The original list words is: {list1}")
print()
print(f"The new list words that have more than 4 letters is: {list2}") 
print()       