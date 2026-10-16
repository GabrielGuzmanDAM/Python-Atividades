# Ejercicio 5
# Muestra los Pokémon que tengan un tipo que acabe en “a”.

def ejercicio5():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo.endswith("a"):
                print(f"{pokemon['nombre']} {tipo}")


if __name__ == "__main__":
    ejercicio5()
