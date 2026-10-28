# Ejercicio 1
# Muestra una lista con los títulos de las series que sean de Animación.

def ejercicio01():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 01")
    print("----------------------------------")

    serie = [s["titulo"] for s in series for g in s["generos"] if g == "Animación"]

    print(f"{serie}")

# Ejercicio 2
# Muestra los títulos de las series que sean de Fantasía o Misterio.

def ejercicio02():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    serie = [s["titulo"] for s in series for g in s["generos"] if g == "Fantasía" or g == "Misterio"]

    print(f"{serie}")

# Ejercicio 3
# Muestra los títulos de las series que tengan una nota igual o superior a 9 y que además tengan 3 o más géneros.

def ejercicio03():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    serie = [s["titulo"] for s in series if len(s["generos"]) >= 3 and s["nota"] >= 9]

    print(f"{serie}")

# Ejercicio 4
# Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el usuario Elena.

def ejercicio04():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 04")
    print("----------------------------------")

    serie = [( s["titulo"], r["nota"] ) for s in series for r in s["reseñas"] if r["usuario"] == "Elena"]

    print(f"{serie}")

# Ejercicio 5
# Muestra una lista con los comentarios que tengan más de 40 caracteres.

def ejercicio05():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 05")
    print("----------------------------------")

    serie = [ r["comentario"] for s in series for r in s["reseñas"] if len(r["comentario"]) > 40]

    print(f"{serie}")

# Ejercicio 6
# Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para todas las series.

def ejercicio06():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 06")
    print("----------------------------------")

    serie = [ ("La serie " + s["titulo"] + " tiene " + str(len(s["reseñas"])) + " reseñas") for s in series]

    print(f"{serie}")

# Ejercicio 7
# Muestra una lista de tuplas (titulo_serie, comentario) para todas las reseñas que hayan dado una puntuación de 10.

def ejercicio07():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 07")
    print("----------------------------------")

    serie = [( s["titulo"], r["comentario"] ) for s in series for r in s["reseñas"] if r["nota"] == 10]

    print(f"{serie}")

# Ejercicio 8
# Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso contrario.

def ejercicio08():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 08")
    print("----------------------------------")

    serie = [(s["titulo"], "Obra maestra" if sum(r["nota"] for r in s["reseñas"]) / len(s["reseñas"]) >= 9 else "Gran serie") for s in series]

    print(f"{serie}")



# Ejercicio 9
# Muestra una lista con todos los géneros de todas las series. No importa si hay géneros duplicados.

def ejercicio09():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 09")
    print("----------------------------------")

    serie = [g for s in series for g in s["generos"]]

    print(f"{serie}")

# Ejercicio 10
# Muestra una lista con todos los nombres de los usuarios que hayan opinado en alguna serie de Drama. No importa si hay nombres repetidos.

def ejercicio10():
    import datos

    series = datos.series

    print("----------------------------------")
    print("EJERCICIO 10")
    print("----------------------------------")

    serie = [r["usuario"] for s in series for r in s["reseñas"] for g in s["generos"] if g == "Drama"]

    print(f"{serie}")