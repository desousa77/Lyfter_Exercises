def personal_information():
    name = "Alvaro De Sousa"
    age = 41
    print()
    print("*** Personal Information ***")
    print("Full Name: ", name)
    print("Age: ", age)
    professional_information()
    
def professional_information():
    profession= "Systems Engineer"
    experience_years = 5    
    print("*** Professional Information ***") 
    print(f"Profession: {profession}")
    print(f"My experience years: {experience_years}") 
    print()

personal_information()
