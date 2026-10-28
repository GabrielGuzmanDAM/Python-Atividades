# Ejercicio 1
# Muestra una lista solo con los nombres de todos los futbolistas.

def ejercicio01():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 01")
    print("----------------------------------")

    listafutbolistasNombres = [j["nombre"] for j in jugadores]

    print(f"{listafutbolistasNombres}")

# Ejercicio 2
# Muestra la lista de los jugadores que llevan el dorsal número 10.

def ejercicio02():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    listaFutbolistasNumero10 = [j for j in jugadores if j["dorsal"] == 10]

    print(f"{listaFutbolistasNumero10}")

# Ejercicio 3
# Muestra una lista con los nombres de los jugadores que pertenecen al "FC Barcelona".

def ejercicio03():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    listaNombresFutbolistasFCBarcelona = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]

    print(f"{listaNombresFutbolistasFCBarcelona}")

# Ejercicio 4
# Muestra una lista con los nombres de los jugadores que tienen una puntuación de pase igual o superior a 9 en sus atributos.

def ejercicio04():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 04")
    print("----------------------------------")

    listaNombresFutbolistasPuntuacion9Pase = [j["nombre"] for j in jugadores if j["atributos"]["pase"] > 9]

    print(f"{listaNombresFutbolistasPuntuacion9Pase}")

# Ejercicio 5
# Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".

def ejercicio05():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 05")
    print("----------------------------------")

    listaJugadoresRuleta = [j for j in jugadores if "ruleta" in j["filigranas"] ]

    print(f"{listaJugadoresRuleta}")

# Ejercicio 6
# Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9.

def ejercicio06():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 06")
    print("----------------------------------")

    listaJugadoresTiro8YRegate9 = [j for j in jugadores if j["atributos"]["tiro"] >= 8 and j["atributos"]["regate"] >= 9]

    print(f"{listaJugadoresTiro8YRegate9}")

# Ejercicio 7
# Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada jugador. Muéstrala.

def ejercicio07():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 07")
    print("----------------------------------")

    listaNombreEquipo = [(j["nombre"] + " (" + j["equipo"] + ")") for j in jugadores]

    print(f"{listaNombreEquipo}")

# Ejercicio 8
# Crea una lista de tuplas con el nombre del jugador y el texto "Goleador" si su atributo de tiro es mayor o igual a 9, o "Asistente" en caso contrario. Muéstrala.

def ejercicio08():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 08")
    print("----------------------------------")

    ListaJugadoresNombresGoleadorOAistente = [(j["nombre"], "SGoleador " if j["atributos"]["tiro"] >= 9 else "Asistente") for j in jugadores]

    print(f"{ListaJugadoresNombresGoleadorOAistente}")

# Ejercicio 9
# Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas distintas.

def ejercicio09():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 09")
    print("----------------------------------")

    ListaJugadoresNombresFiligranas2 = [j["nombre"] for j in jugadores if len(j["filigranas"]) > 2]

    print(f"{ListaJugadoresNombresFiligranas2}")

# Ejercicio 10
# Extrae en una única lista todas las filigranas de todos los jugadores (no importa si hay duplicadas) y muéstrala.

def ejercicio10():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 10")
    print("----------------------------------")

    ListaJugadoresFiligranas= [f for j in jugadores for f in j["filigranas"]]

    print(f"{ListaJugadoresFiligranas}")