# Ejercicio 12
# Elimina todos los personajes cuya raza sea Demonio.

def ejercicio12():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren[:]:
        if personaje["raza"] == "Demonio":
            print(f"Demonio eliminado: {personaje}")
            personajes_frieren.remove(personaje)

    print("\nPersonajes restantes:")
    for personaje in personajes_frieren:
        print(personaje["nombre"])


if __name__ == "__main__":
    ejercicio12()
