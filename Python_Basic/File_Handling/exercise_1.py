def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as songs_file:
        songs = songs_file.readlines()
        print()
        print("*** Reading the Original Song List File. ***\n" )            
        for index, song in enumerate(songs, start=1):            
            print(f"Song {index}: {song.strip()}")
    return songs

def order_original_file(list_to_order):
    sorted_songs = sorted(list_to_order, key=str.lower)
    return sorted_songs    

def write_new_song_list(file_name, song_list):
    with open(file_name, 'w', encoding='utf-8') as new_song_file:
        new_song_file.writelines(song_list)
        print()
        print(f"*** The new .txt file: {file_name}. Was created with the song list sorted alphabetically. ")
        print()
        
def main():
    original_songs = read_file('songs_list.txt')
    sorted_songs = order_original_file(original_songs)
    write_new_song_list('New_song_list.txt', sorted_songs)

if __name__ == "__main__":
    main()