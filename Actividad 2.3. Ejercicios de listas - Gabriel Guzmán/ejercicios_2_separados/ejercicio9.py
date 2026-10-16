# Ejercicio 9
# Muestra el nombre y la raza de los personajes que sean magos de primera clase.

def ejercicio9():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if "Magos de Primera Clase" in personaje["afiliacion"]:
            print(f"{personaje['nombre']} {personaje['raza']}")


if __name__ == "__main__":
    ejercicio9()
