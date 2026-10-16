# Ejercicio 11
# Inserta un nuevo personaje al final de la lista y muestra la lista.

def ejercicio11():
    import datos
    import importlib
    importlib.reload(datos)
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


if __name__ == "__main__":
    ejercicio11()
