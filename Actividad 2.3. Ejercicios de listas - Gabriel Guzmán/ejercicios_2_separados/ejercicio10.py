# Ejercicio 10
# Muestra el nombre, la raza y la edad de los personajes del Grupo de los Cuatro Héroes.

def ejercicio10():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if "Grupo de los Cuatro Héroes" in personaje["afiliacion"]:
            print(f"{personaje['nombre']} {personaje['raza']} {personaje['edad']}")


if __name__ == "__main__":
    ejercicio10()
