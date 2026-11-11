def hotel_data():
    hotel_information = {
        'hotel_name': 'Hilton',
        'star_rating': 4.5,
        'rooms': [
            {
            'room_number': 225,
            'floor': 2,
            'price_per_night': 180
            },
            {
            'room_number': 331,
            'floor': 3,
            'price_per_night': 245.00
            }
        ]
    }
    return hotel_information

def show_hotel_information():
    hotel_info = hotel_data()
    print()
    print(hotel_info)  # print all dictionary
    print()
    print(hotel_info['rooms'][0])  # print only room 225
    print()
    print(hotel_info['rooms'][1]) 
    
def main():
    hotel_data() # print only room 331
    show_hotel_information() # print all dictionary and room 225 and 331

if __name__ == "__main__":
    main()