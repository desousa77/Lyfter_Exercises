import json

def read_pokemon_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as poke_file:
        poke_data = json.load(poke_file)
    return poke_data

def group_pokemon_by_type(poke_info):
    pokemon_group ={}
    for pokemon in poke_info:
        pokemon_type = pokemon['type'].upper()
        if pokemon_type not in pokemon_group:
            pokemon_group[pokemon_type] = []
        pokemon_group[pokemon_type].append(pokemon['level'])
    return pokemon_group 

def calculate_avg_level(poke_data):
    file_group = {}
    for pokemon_type, levels in poke_data.items():
        avg_level = sum(levels) / len(levels)
        file_group[pokemon_type] = avg_level
    return file_group    

def show_results(avg_dir):
    print("\nAverage Pokemon level by Type: ")
    for pokemon_type, avg_level in avg_dir.items():
        print("____________________________________")
        print(f"\t* {pokemon_type}: {avg_level} ")        
    print()
        
def main():
    input_file = 'Pokemon_file.json'
    reader_file = read_pokemon_file(input_file)
    get_poke_group = group_pokemon_by_type(reader_file)
    get_avg_dir = calculate_avg_level(get_poke_group)
    show_results(get_avg_dir)


if __name__ =='__main__':
    main()