employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofia", "email": "sofia@empresa.com", "department": "RRHH"},
]
grouped = {}

for index in employees:
    department = index['department']
    if department not in grouped:
        grouped[department] = []
        
    grouped[department].append(index)

for index_group in grouped:
    print("Department: ", index_group, "/ Employees: ", grouped[index_group])

