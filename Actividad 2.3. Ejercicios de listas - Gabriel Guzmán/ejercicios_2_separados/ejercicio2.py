# Ejercicio 2
# Muestra el nombre y la altura de los Pokémon que midan menos que la media.

def ejercicio2():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    alturaSumas = 0
    for pokemon in pokemons:
        alturaSumas += pokemon["altura_m"]

    alturaMedia = alturaSumas / len(pokemons)

    for pokemon in pokemons:
        if pokemon["altura_m"] < alturaMedia:
            print(f"{pokemon['nombre']} {pokemon['altura_m']}")


if __name__ == "__main__":
    ejercicio2()
