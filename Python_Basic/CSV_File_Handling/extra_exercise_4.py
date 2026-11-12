import csv

def read_video_games_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)       
        developer = get_user_developer().upper()
        developer_found = False
        print(f"\n Video games developer by: {developer}")
        for search in reader:
            if developer == search[2].upper():
                print(f"\nName: {search[0]}, (ESRB rating: {search[3]}, Genre: {search[1]} )")
                developer_found = True
        
        if not developer_found:
            print(f"\n The developer: {developer}, was not found.")

def get_user_developer():
    user_developer = input("Please enter the developer name to find: ")
    return user_developer 

def main():
    file_path = 'Video_Game_Information.csv'
    read_video_games_csv(file_path)

if __name__ == '__main__':
    main()   