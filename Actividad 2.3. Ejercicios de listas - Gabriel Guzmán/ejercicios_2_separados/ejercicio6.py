# Ejercicio 6
# Inserta un nuevo Pokémon al final de la lista y muestra la lista.

def ejercicio6():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    pokemons.append({
        "nombre": "Psyduck",
        "generacion": 1,
        "categoria": "Pato",
        "tipos": ["Agua"],
        "peso_kg": 19.6,
        "altura_m": 0.8
    })

    for pokemon in pokemons:
        print(pokemon)


if __name__ == "__main__":
    ejercicio6()
