# Ejercicio 4
# Pedir al usuario un número y mostrar el triángulo de Pascal de ese número de filas.
# Si el número es inferior a 1, mostrar un mensaje de error.

def factorial(x):
    if x == 0:
        return 1
    else:
        resultado = x * factorial(x - 1)
        return resultado


def ejercicio4():
    n = None

    while n is None:
        try:
            n = int(input("Introduce el número de filas para el triángulo de Pascal (entero mayor o igual a 1): "))
            if n < 1:
                print("Error: el número debe ser mayor o igual a 1.")
                n = None
        except ValueError:
            print("Error: por favor, introduce un número entero válido.")

    for i in range(n):
        for j in range(n - i + 1):
            print(" ", end="")
        for j in range(i + 1):
            print(f"{factorial(i) // (factorial(j) * factorial(i - j))} ", end="")
        print()


if __name__ == "__main__":
    ejercicio4()
