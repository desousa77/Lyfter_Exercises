import json

def read_pokemon_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as poke_file:
        reader_data = json.load(poke_file)
    return reader_data

def show_pokemon_data(data):
    print("\nThese are the Pokemon currently in the JSON file: \n")
    for index, pokemon_data in enumerate(data, start=1):
        print(f"{index}. Name: {pokemon_data['name']}")
        print(f"\t * Type: {pokemon_data['type']}")
        print(f"\t * Level: {pokemon_data['level']}")
        print(f"\t * Weight in kg: {pokemon_data['weight_kg']}\n")


def main():
    input_file = 'Pokemon_file.json'
    reader_pokemon = read_pokemon_data(input_file)
    show_pokemon_data(reader_pokemon)

if __name__ == '__main__':
    main()