list_a=['first_name', 'last_name', 'role']
list_b=['Alvaro', 'De Sousa', 'Software Engineer']
personal_information = {}

for index in range (len(list_a)):
    personal_information[list_a[index]] = list_b[index]
print()
print("New Dictionary: ", personal_information)
print()
print("First Name: ", personal_information.get('first_name'))
print()
print("Last Name: ", personal_information.get('last_name'))
print()
print("Role: ", personal_information.get('role'))
print()