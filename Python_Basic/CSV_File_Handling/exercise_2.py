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

def write_cvs_file(file_path, csv_file):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = csv_file[0].keys()
        write = csv.DictWriter(file, fieldnames=headers, delimiter=get_delimiter_file())
        write.writeheader()
        write.writerows(csv_file)
        print()
        print(f"The CSV file: {file_path}, was create successfully.!!!") 
        print()       
    
def get_delimiter_file():
    print()
    print("Please select an option to set the file delimiter.!!!")
    print()
    print(
            "Option 1 (Space)\n"
            "Option 2 (\\t)\n"
            "Option 3 (|)\n"
            "Option 4 (,)\n")
    while True:
        try:
            option = int(input("Please enter your option:  "))
            if 1<= option <= 4:
                if option ==1:
                    user_option = ' '
                elif option==2:
                    user_option = '\t'
                elif option==3:
                    user_option= '|'
                else:
                    user_option= ','            
                break
            else:
                print("Please enter a valid option.!!!")
        except ValueError:
            print(f"Invalid input, please enter an option between 1 and 4 ")        
    return user_option

def main():
    
    input_file='Alternative_Version_Video_Game_Information.csv'
    video_game_data = get_video_game_data()
    write_cvs_file(input_file, video_game_data)

if __name__ == '__main__':
    main()