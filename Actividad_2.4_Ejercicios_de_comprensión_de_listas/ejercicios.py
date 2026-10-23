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

    listaNombresFutbolistasPuntuacion9Pase = [j["nombre"] for j in jugadores["atributos"] if j["pase"] > 9]

    print(f"{listaNombresFutbolistasPuntuacion9Pase}")

def ejercicio05():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 05")
    print("----------------------------------")

def ejercicio06():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 06")
    print("----------------------------------")

def ejercicio07():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 07")
    print("----------------------------------")

def ejercicio08():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 08")
    print("----------------------------------")

def ejercicio09():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 09")
    print("----------------------------------")

def ejercicio10():
    import datos

    jugadores = datos.jugadores

    print("----------------------------------")
    print("EJERCICIO 10")
    print("----------------------------------")