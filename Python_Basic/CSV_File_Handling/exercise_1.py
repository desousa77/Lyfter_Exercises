import csv

def get_video_game_data():
    video_game_data_list = []
    while True:
        print("Please, Enter the information requested below: \n ")

        game_name = input("Enter the video game NAME: ")
        game_genre = input("Enter the video game GENRE: ")
        game_developer = input("Enter the video game DEVELOPER: ")
        game_rating = input("Enter the video game ESRB RATING: ")
        
        video_game_data = {
            'Name': game_name,
            'Genre': game_genre,
            'Developer': game_developer,
            'ESRB_Rating': game_rating
        }

        video_game_data_list.append(video_game_data)    
        
        add_another_game = input("Do you want to add another video game? (Y/N): ").upper()
        if add_another_game =='N':
            break
    
    return video_game_data_list

def write_csv_file(file_path, csv_file):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = csv_file[0].keys()
        write = csv.DictWriter(file, fieldnames=headers)
        write.writeheader()
        write.writerows(csv_file)
        print()
        print(f"The CSV file: {file_path}, was create successfully.!!!") 
        print()       
    
def main():
    input_file='Video_Game_Information.csv'
    
    video_game_data = get_video_game_data()
    write_csv_file(input_file, video_game_data)

if __name__ == '__main__':
    main()