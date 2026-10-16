# main.py
# Menú principal para ejecutar los 15 ejercicios.

from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio3 import ejercicio3
from ejercicio4 import ejercicio4
from ejercicio5 import ejercicio5
from ejercicio6 import ejercicio6
from ejercicio7 import ejercicio7
from ejercicio8 import ejercicio8
from ejercicio9 import ejercicio9
from ejercicio10 import ejercicio10
from ejercicio11 import ejercicio11
from ejercicio12 import ejercicio12
from ejercicio13 import ejercicio13
from ejercicio14 import ejercicio14
from ejercicio15 import ejercicio15


def main():
    ejercicios = {
        "1": ("Media de altura de los Pokémon", ejercicio1),
        "2": ("Pokémon por debajo de la altura media", ejercicio2),
        "3": ("Pokémon con más peso", ejercicio3),
        "4": ("Pokémon de tipo Agua", ejercicio4),
        "5": ("Tipos que terminan en 'a'", ejercicio5),
        "6": ("Añadir un Pokémon", ejercicio6),
        "7": ("Eliminar Pokémon de tipo Normal", ejercicio7),
        "8": ("Edad media de personajes humanos", ejercicio8),
        "9": ("Magos de Primera Clase", ejercicio9),
        "10": ("Grupo de los Cuatro Héroes", ejercicio10),
        "11": ("Añadir un personaje", ejercicio11),
        "12": ("Eliminar personajes Demonio", ejercicio12),
        "13": ("Añadir afiliación a los elfos", ejercicio13),
        "14": ("Quitar afiliación de la Asociación Continental de Magia", ejercicio14),
        "15": ("Cambiar humanos de 100 años o más a Zombie", ejercicio15),
    }

    while True:
        print("\n===== MENÚ DE EJERCICIOS =====")
        for numero, (descripcion, _) in ejercicios.items():
            print(f"{numero}. {descripcion}")
        print("0. Salir")

        opcion = input("Elige un ejercicio: ").strip()

        if opcion == "0":
            print("Saliendo del programa...")
            break

        ejercicio = ejercicios.get(opcion)
        if ejercicio:
            print(f"\n--- {ejercicio[0]} ---")
            ejercicio[1]()
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
