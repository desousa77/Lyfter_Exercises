import json

def read_pokemon_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        read_json = json.load(json_file)
    return read_json

def show_pokemon_data(data):    
        print("\nThere are the Pokemon currently stored in the JSON file:\n")
        for pokemon in data:
            print(f"\nPokemon Name: {pokemon['name']} | Pokemon Type: {pokemon['type']}")
            print(f"Level: {pokemon['level']}")
            print(f"weight_kg: {pokemon['weight_kg']}")
            print(f"is_shiny: {pokemon['is_shiny']}")
            print(f"held_item: {pokemon['held_item']}")
            print("Skills: ")
            for pokemon_skill in pokemon['skills']:
                print(f" - {pokemon_skill}")
            print("stats: ")
            for stat, value in pokemon['stats'].items():
                print(f" - {stat}: {value}")

def get_new_pokemon_data():
    print("\nEnter the information to add a new Pokemon\n")
    name = input("Enter the pokemon name: ")
    pokemon_type = input("Enter the pokemon type: ")
    level = int(input("Enter the pokemon level: "))
    weight = float(input("Enter the pokemon weight in kg: "))
    shiny = input("Is this pokemon shiny? (True/False): ")
    held = input("Enter pokemon held: ")
    skills = input("Enter the pokemon's skills separated by commas: ").split(",")
    stats ={
        "hp": int(input("Enter HP: ")),
        "attack": int(input("Enter attack: ")),
        "defense": int(input("Enter defense: ")),
        "sp_attack": int(input("Enter special attack: ")),
        "sp_defense": int(input("Enter special defense: ")),
        "speed": int(input("Enter speed: "))
        }
    
    pokemon_data={
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight,
        "is_shiny": shiny,
        "held_item": held,
        "skills": skills,
        "stats": stats
    }

    return pokemon_data

def save_new_pokemon(file_path, poke_data, new_poke):
    new_json = poke_data
    new_json.append(new_poke)
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(new_json, json_file, indent=4)
        print("\nThe new record was added successfully.\n")
            
def main():
    input_file = 'Pokemon_file.json'
    pokemon_data = read_pokemon_file(input_file)
    show_pokemon_data(pokemon_data)
    new_poke_data = get_new_pokemon_data()
    save_new_pokemon(input_file, pokemon_data, new_poke_data) 
    
if __name__ == '__main__':
    main()