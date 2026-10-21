# Ejercicio 1
# Muestra la media de altura de todos los Pokémon.

def ejercicio01():
    import datos

    pokemons = datos.pokemons

    print("----------------------------------")
    print("EJERCICIO 01")
    print("----------------------------------")

    media = sum(p['altura_m'] for p in pokemons) / len(pokemons)

    print(f"La altura media de los Pokémon es: {media}")

# Ejercicio 2
# Muestra el nombre y la altura de los Pokémon que midan menos que la media.

def ejercicio02():
    import datos

    pokemons = datos.pokemons

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    pokemosMenorMediaAltura = [p for p in pokemons if p['altura_m'] < sum(p['altura_m'] for p in pokemons) / len(pokemons)]

    for pokemon in pokemosMenorMediaAltura:
        print(f"{pokemon['nombre']} {pokemon['altura_m']}")

# Ejercicio 3
# Muestra en una sola línea el nombre y el peso del Pokémon con más peso.

def ejercicio03():
    import datos

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    pokemons = datos.pokemons

    pokemonPesoMaximo = [p for p in pokemons if p["peso_kg"] == max(pokemon["peso_kg"] for pokemon in pokemons)]

    print(f"{pokemonPesoMaximo["peso_kg"]}")

# Ejercicio 4
# Muestra el nombre y los tipos de los Pokémon que sean de tipo Agua.

def ejercicio04():
    import datos

    print("----------------------------------")
    print("EJERCICIO 04")
    print("----------------------------------")

    pokemons = datos.pokemons

    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo == "Agua":
                print(f"{pokemon['nombre']} {tipo}")

# Ejercicio 5
# Muestra los Pokémon que tengan un tipo que acabe en “a”.

def ejercicio05():
    import datos

    print("----------------------------------")
    print("EJERCICIO 05")
    print("----------------------------------")

    pokemons = datos.pokemons

    for pokemon in pokemons:
        for tipo in pokemon["tipos"]:
            if tipo.endswith("a"):
                print(f"{pokemon['nombre']} {tipo}")

# Ejercicio 6
# Inserta un nuevo Pokémon al final de la lista y muestra la lista.

def ejercicio06():
    import datos

    print("----------------------------------")
    print("EJERCICIO 06")
    print("----------------------------------")

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

# Ejercicio 7
# Elimina todos los Pokémon de tipo Normal.

def ejercicio07():
    import datos

    print("----------------------------------")
    print("EJERCICIO 07")
    print("----------------------------------")

    pokemons = datos.pokemons

    for pokemon in pokemons[:]:
        if "Normal" in pokemon["tipos"]:
            print(f"Pokémon eliminado: {pokemon}")
            pokemons.remove(pokemon)

    print("\nPokémon restantes:")
    for pokemon in pokemons:
        print(pokemon["nombre"])

# Ejercicio 8
# Muestra la edad media de los personajes humanos.

def ejercicio08():
    import datos

    print("----------------------------------")
    print("EJERCICIO 08")
    print("----------------------------------")

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

# Ejercicio 9
# Muestra el nombre y la raza de los personajes que sean magos de primera clase.

def ejercicio09():
    import datos

    print("----------------------------------")
    print("EJERCICIO 09")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if "Magos de Primera Clase" in personaje["afiliacion"]:
            print(f"{personaje['nombre']} {personaje['raza']}")

# Ejercicio 10
# Muestra el nombre, la raza y la edad de los personajes del Grupo de los Cuatro Héroes.

def ejercicio10():
    import datos

    print("----------------------------------")
    print("EJERCICIO 10")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if "Grupo de los Cuatro Héroes" in personaje["afiliacion"]:
            print(f"{personaje['nombre']} {personaje['raza']} {personaje['edad']}")

# Ejercicio 11
# Inserta un nuevo personaje al final de la lista y muestra la lista.

def ejercicio11():
    import datos

    print("----------------------------------")
    print("EJERCICIO 11")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren

    personajes_frieren.append({
        "nombre": "Laufen",
        "raza": "Humano",
        "clase": "Mago",
        "edad": 20,
        "afiliacion": ["Magos de Primera Clase"]
    })

    for personaje in personajes_frieren:
        print(personaje)

# Ejercicio 12
# Elimina todos los personajes cuya raza sea Demonio.

def ejercicio12():
    import datos

    print("----------------------------------")
    print("EJERCICIO 12")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren[:]:
        if personaje["raza"] == "Demonio":
            print(f"Demonio eliminado: {personaje}")
            personajes_frieren.remove(personaje)

    print("\nPersonajes restantes:")
    for personaje in personajes_frieren:
        print(personaje["nombre"])

# Ejercicio 13
# Añade a todos los elfos la afiliación indicada.

def ejercicio13():
    import datos

    print("----------------------------------")
    print("EJERCICIO 13")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren
    nueva_afiliacion = "Elfos Supervivientes del Examen de Python"

    for personaje in personajes_frieren:
        if personaje["raza"] == "Elfo":
            if nueva_afiliacion not in personaje["afiliacion"]:
                personaje["afiliacion"].append(nueva_afiliacion)
            print(f"{personaje['nombre']} {personaje['raza']} {personaje['afiliacion']}")

# Ejercicio 14
# Quita la afiliación “Asociación Continental de Magia” a quienes la tengan.

def ejercicio14():
    import datos

    print("----------------------------------")
    print("EJERCICIO 14")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren
    afiliacion_a_quitar = "Asociación Continental de Magia"

    for personaje in personajes_frieren:
        if afiliacion_a_quitar in personaje["afiliacion"]:
            personaje["afiliacion"].remove(afiliacion_a_quitar)
            print(personaje)

# Ejercicio 15
# Cambia a “Zombie” la raza de los humanos que tengan 100 años o más.

def ejercicio15():
    import datos

    print("----------------------------------")
    print("EJERCICIO 15")
    print("----------------------------------")

    personajes_frieren = datos.personajes_frieren

    for personaje in personajes_frieren:
        if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
            personaje["raza"] = "Zombie"
            print(personaje)