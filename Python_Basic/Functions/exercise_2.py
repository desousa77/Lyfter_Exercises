number3 = 40
def fuc_2numbers():
    number1 = 10
    number2 = 20    
    print(f"The Number #1 is: {number1}, The Number #2 is: {number2}")

print(f"Try to print Number #1: {number1}") # podemos ver que no puedo acceder a una variable de una funcion desde afuera de ella.
fuc_2numbers()

def fuc_global_number():
    global number3 #sin esta declaracion no puedo cambiar el valor de la variable global dentro de la funcion
    number3=20

fuc_global_number()
print(f"The Number #3 is: {number3}")