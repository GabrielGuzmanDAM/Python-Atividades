# Archivo principal: menú para ejecutar los ejercicios.

from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio3 import ejercicio3
from ejercicio4 import ejercicio4


def main():
    while True:
        print("\n===== MENÚ DE EJERCICIOS =====")
        print("1. Sumatorio")
        print("2. Factorial")
        print("3. Potencia")
        print("4. Triángulo de Pascal")
        print("0. Salir")

        opcion = input("Elige un ejercicio: ").strip()

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
