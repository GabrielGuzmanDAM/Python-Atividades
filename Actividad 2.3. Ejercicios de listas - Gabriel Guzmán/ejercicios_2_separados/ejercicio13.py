# Ejercicio 13
# Añade a todos los elfos la afiliación indicada.

def ejercicio13():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren
    nueva_afiliacion = "Elfos Supervivientes del Examen de Python"

    for personaje in personajes_frieren:
        if personaje["raza"] == "Elfo":
            if nueva_afiliacion not in personaje["afiliacion"]:
                personaje["afiliacion"].append(nueva_afiliacion)
            print(f"{personaje['nombre']} {personaje['raza']} {personaje['afiliacion']}")


if __name__ == "__main__":
    ejercicio13()
