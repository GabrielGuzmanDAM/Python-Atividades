# Ejercicio 1
# Muestra la media de altura de todos los Pokémon.

def ejercicio1():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    alturaSumas = 0
    for pokemon in pokemons:
        alturaSumas += pokemon["altura_m"]

    alturaMedia = alturaSumas / len(pokemons)
    print(f"La altura media de los Pokémon es: {alturaMedia}")


if __name__ == "__main__":
    ejercicio1()
