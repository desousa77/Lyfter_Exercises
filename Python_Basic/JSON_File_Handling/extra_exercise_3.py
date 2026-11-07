import json

def read_pokemon_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader_poke = json.load(file)
    return reader_poke

def get_pokemon_stats(data_poke):
    poke_stats =[]
    
    for pokemon in data_poke:
        pokemon_info = {
            'name': pokemon['name'],
            'stats': pokemon['stats']
        }

        poke_stats.append(pokemon_info)

    return poke_stats    

def show_pokemon_data(pokemon_data):
    print("\nThere are the existing Pokemon and their stats:\n")
    for index, pokemon in enumerate(pokemon_data, start=1):
        print(f"{index}. Pokemon: {pokemon['name']}")

        for stat_name, stat_value in pokemon['stats'].items():
            print(f"\t* {stat_name}: {stat_value}")
        print("******************************************************")

def main():
    input_file = 'Pokemon_file.json'
    reader_data = read_pokemon_file(input_file)
    get_poke_data = get_pokemon_stats(reader_data)
    show_pokemon_data(get_poke_data)

if __name__ == '__main__':
    main()  