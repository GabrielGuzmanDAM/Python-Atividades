# Ejercicio 3
# Pedir al usuario la edad de una persona y mostrar si es mayor o menor de edad. Si
#la edad es menor a 0 mostrar un mensaje de error, y si es superior a 120 indicar que
#es un vampiro.

edad = None;

while edad == None:
    try:
        edad = int(input("Introduce la edad de la persona: "))
    except ValueError:
        edad = None

s