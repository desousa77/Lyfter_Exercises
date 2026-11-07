import csv

def read_video_game_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader =csv.reader(csv_file)
        rating = get_user_esrb()
        print("\nVideo Games Information:\n")
        next(reader, None)
        game_found = False
        for game in reader:
            if rating == game[3]:
                print(
                    f"Name: {game[0]}\n"
                    f"Genre: {game[1]}\n"
                    f"Developer: {game[2]}\n"
                    f"ESRB Rating: {game[3]}\n"
                    )
                game_found = True         

        if not game_found:
            print("\n No video games were found with that ESRB rating.")        
                
def get_user_esrb():
    user_esrb = input("Please enter the ESRB rating to find: ").upper()
    return user_esrb

def main():
    file_input = 'Video_Game_Information.csv'
    read_video_game_csv(file_input)

if __name__ == '__main__':
    main()