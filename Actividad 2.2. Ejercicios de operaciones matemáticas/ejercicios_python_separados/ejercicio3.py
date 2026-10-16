# Ejercicio 3
# Pedir al usuario dos números enteros (base y potencia). Calcular el resultado de
# elevar la base al exponente. Mostrar un error si la base es menor que 1
# o si la potencia es menor que 0.

def ejercicio3():
    base = None
    potencia = None

    while base is None:
        try:
            base = int(input("Introduce la base (entero mayor o igual a 1): "))
            if base < 1:
                print("Error: la base debe ser mayor o igual a 1.")
                base = None
        except ValueError:
            print("Error: por favor, introduce un número entero válido.")

    while potencia is None:
        try:
            potencia = int(input("Introduce la potencia (entero mayor o igual a 0): "))
            if potencia < 0:
                print("Error: la potencia debe ser mayor o igual a 0.")
                potencia = None
        except ValueError:
            print("Error: por favor, introduce un número entero válido.")

    resultado = base ** potencia
    print(f"El resultado de {base} elevado a {potencia} es: {resultado}")


if __name__ == "__main__":
    ejercicio3()
