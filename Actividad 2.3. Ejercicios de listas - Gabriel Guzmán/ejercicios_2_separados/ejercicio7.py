# Ejercicio 7
# Elimina todos los Pokémon de tipo Normal.

def ejercicio7():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    for pokemon in pokemons[:]:
        if "Normal" in pokemon["tipos"]:
            print(f"Pokémon eliminado: {pokemon}")
            pokemons.remove(pokemon)

    print("\nPokémon restantes:")
    for pokemon in pokemons:
        print(pokemon["nombre"])


if __name__ == "__main__":
    ejercicio7()
