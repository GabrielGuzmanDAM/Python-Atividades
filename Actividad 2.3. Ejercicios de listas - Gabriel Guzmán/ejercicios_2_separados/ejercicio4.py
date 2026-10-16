# Ejercicio 4
# Muestra el nombre y los tipos de los Pokémon que sean de tipo Agua.

def ejercicio4():
    import datos
    import importlib
    importlib.reload(datos)
    pokemons = datos.pokemons

    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo == "Agua":
                print(f"{pokemon['nombre']} {tipo}")


if __name__ == "__main__":
    ejercicio4()
