import csv

def read_video_games_csv(file_path):
    games_by_genre = {}        
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
    
        for games_genre in reader:
            genre = games_genre[1]
            if genre in games_by_genre:
                games_by_genre[genre] +=1
            else:
                games_by_genre[genre] = 1
    
    return games_by_genre

def show_data(video_games_data):
    for genre, count in sorted(video_games_data.items()):
        print(f"{genre}: {count} games." ) 

def main():
    file_input = 'Video_Game_Information.csv'
    games_data = read_video_games_csv(file_input)
    show_data(games_data)

if __name__ == '__main__':
    main()