from datos import personajes

def ejercicio01():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 01")
    print("----------------------------------")

    personaje = [p["nombre"] for p in personajes if p["afiliacion"] == "Policía de Raccoon City" and p["vivo"] == True]

    print(f"{personaje}")

def ejercicio02():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    personaje = [p for p in personajes for a in p["armas"] if a == "Pistola Samurai Edge"]

    personaje2 = [p["nombre"] for p in personaje for a in p["armas"] if a == "Lanzagranadas"]

    print(f"{personaje2}")

def ejercicio03():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    personaje = [(p["nombre"] , p["afiliacion"]) for p in personajes if p["afiliacion"] != "Policía de Raccoon City"]

    print(f"{personaje}")

def ejercicio04():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 04")
    print("----------------------------------")

    personaje = [(p["nombre"] + " (" + p["afiliacion"] + ")") for p in personajes if p["registro_misiones"]["misiones_completadas"] > 20]

    print(f"{personaje}")

def ejercicio05():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 05")
    print("----------------------------------")

    personaje = [(p["nombre"] , (p["estatura_m"] * 100)) for p in personajes if p["estatura_m"] > 1.7]

    print(f"{personaje}")

def ejercicio06():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 06")
    print("----------------------------------")

    personaje = [a for p in personajes for a in p["armas"]]

    print(f"{personaje}")

def ejercicio07():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 07")
    print("----------------------------------")

    personaje = [p["nombre"] for p in personajes if p["registro_misiones"]["zombies_solo"] +  p["registro_misiones"]["zombies_equipo"] > 100]

    print(f"{personaje}")

def ejercicio08():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 08")
    print("----------------------------------")

    personaje = [(p["nombre"] , (p["registro_misiones"]["zombies_solo"] +  p["registro_misiones"]["zombies_equipo"])) for p in personajes ]

    print(f"{personaje}")

def ejercicio09():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 09")
    print("----------------------------------")

    alturas = [p["estatura_m"] for p in personajes ]

    media = sum(alturas) / len(personajes)

    print(f"{media}")

def ejercicio10():
    import datos

    personajes = datos.personajes

    print("----------------------------------")
    print("EJERCICIO 10")
    print("----------------------------------")

    alturas = [p["estatura_m"] for p in personajes ]

    media = sum(alturas) / len(personajes)

    personaje = [(p["nombre"] , p["estatura_m"]) for p in personajes if p["estatura_m"] > media]

    print(f"{personaje}")



