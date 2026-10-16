# Ejercicio 8
# Muestra la edad media de los personajes humanos.

def ejercicio8():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren

    humanos = [
        personaje for personaje in personajes_frieren
        if personaje["raza"] == "Humano"
    ]

    if not humanos:
        print("No hay personajes humanos en la lista.")
        return

    edadSumas = 0
    for personaje in humanos:
        edadSumas += personaje["edad"]

    edadMedia = edadSumas / len(humanos)
    print(f"La edad media de los personajes humanos es: {edadMedia}")


if __name__ == "__main__":
    ejercicio8()
