hotel_information ={
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
print()
print(hotel_information)#print all dictionary
print()
print(hotel_information['rooms'][0])# print only room 225
print()
print(hotel_information['rooms'][1])# print only room 331
