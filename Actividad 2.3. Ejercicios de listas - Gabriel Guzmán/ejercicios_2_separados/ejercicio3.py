# Ejercicio 3
# Muestra en una sola línea el nombre y el peso del Pokémon con más peso.

def ejercicio3():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    pesoMaximo = max(pokemon["peso_kg"] for pokemon in pokemons)
    for pokemon in pokemons:
        if pokemon["peso_kg"] == pesoMaximo:
            print(f"{pokemon['nombre']} {pokemon['peso_kg']}")


if __name__ == "__main__":
    ejercicio3()
