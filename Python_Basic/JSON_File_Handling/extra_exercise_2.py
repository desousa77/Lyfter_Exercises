import json

def read_pokemon_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as poke_file:
        pokemon_data = json.load(poke_file)
    return pokemon_data

def find_pokemon_type(data):
    list_type= set()
    for pokemon in data:
        list_type.add(pokemon['type'].upper())
    return sorted(list_type)    

def get_user_pokemon_type(list_poke_type):
    print(f"\nCurrently available Pokemon types: {list_poke_type}\n")
    user_poke_type = input(
        "Please enter the Pokemon type you want to search for: "
        ).upper().strip()
    print()
    return user_poke_type    

def find_pokemon_type_user(poke_data, user_type):
    poke_by_type = []
    for pokemon in poke_data:
        if pokemon['type'].upper() == user_type:
            poke_by_type.append(pokemon)
    return poke_by_type

def show_poke_by_type(poke_list):
    if poke_list:
        
        if len(poke_list) > 1:
            print("The Pokemon of this type currently available are: \n")
        else: print("The Pokemon of this type currently available is: \n")     

        for index, poke_type in enumerate(poke_list, start=1):
            print(f"\t{index}. Name: {poke_type['name']}")
    else:
        print("No Pokemon of this type were found.")        

def main():
    input_file= 'Pokemon_file.json'
    reader_poke_data = read_pokemon_data(input_file)     
    poke_type_list = find_pokemon_type(reader_poke_data)
    user_type_poke = get_user_pokemon_type(poke_type_list)
    result_find = find_pokemon_type_user(reader_poke_data, user_type_poke)
    show_poke_by_type(result_find)

if __name__ == '__main__':
    main()