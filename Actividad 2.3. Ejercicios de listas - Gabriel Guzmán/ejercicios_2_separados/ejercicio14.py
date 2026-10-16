# Ejercicio 14
# Quita la afiliación “Asociación Continental de Magia” a quienes la tengan.

def ejercicio14():
    import datos
    import importlib
    importlib.reload(datos)
    personajes_frieren = datos.personajes_frieren
    afiliacion_a_quitar = "Asociación Continental de Magia"

    for personaje in personajes_frieren:
        if afiliacion_a_quitar in personaje["afiliacion"]:
            personaje["afiliacion"].remove(afiliacion_a_quitar)
            print(personaje)


if __name__ == "__main__":
    ejercicio14()
