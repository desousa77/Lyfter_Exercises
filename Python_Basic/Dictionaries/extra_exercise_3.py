products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_category = {}

for index_category in products:
    category = index_category['category']
    price = index_category['price']

    if category not in total_category:
        total_category[category]=0
    total_category[category] += price

for index_total in total_category:
    print("Category: ", index_total, ", Total: ", total_category[index_total])