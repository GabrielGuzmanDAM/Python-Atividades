# Ejercicio 2
# Pedir al usuario un número entero y calcular el factorial desde 1 hasta dicho número
# (incluido). Si el número introducido es menor que 1, mostrar un mensaje de error.

def ejercicio2():
    numero = None

    while numero is None:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero < 1:
                print("Error: el número debe ser mayor o igual a 1.")
                numero = None
        except ValueError:
            print("Error: por favor, introduce un número entero válido.")

    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i
        print("El factorial de", numero, "es:", factorial)


if __name__ == "__main__":
    ejercicio2()
