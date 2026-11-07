import csv

def read_video_game_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader =csv.reader(csv_file)
        
        print("\nVideo Games Information:\n")
        next(reader, None)
        
        for game in reader:
            print(
                f"Name: {game[0]}\n"
                f"Genre: {game[1]}\n"
                f"Developer: {game[2]}\n"
                f"ESRB Rating: {game[3]}\n"
                )
def main():
    file_input = 'Video_Game_Information.csv'
    read_video_game_csv(file_input)

if __name__ == '__main__':
    main()