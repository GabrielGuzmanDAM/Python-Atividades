# Ejercicio 15
# Cambia a “Zombie” la raza de los humanos que tengan 100 años o más.

def ejercicio15():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
            personaje["raza"] = "Zombie"
            print(personaje)


if __name__ == "__main__":
    ejercicio15()
