EJERCICIOS 1-15 SEPARADOS

Archivos:
- main.py: menú para elegir cualquiera de los 15 ejercicios.
- ejercicio1.py ... ejercicio15.py: un ejercicio por archivo.

IMPORTANTE:
Estos ejercicios importan un módulo llamado datos.py. Coloca tu archivo datos.py
en esta misma carpeta. Debe contener las listas:
- pokemons
- personajes_frieren

No se incluye datos.py porque no venía dentro del notebook adjunto.

Cómo ejecutar:
1. Descomprime el ZIP.
2. Coloca datos.py en la misma carpeta que main.py y los ejercicios.
3. Abre una terminal en esa carpeta.
4. Ejecuta: python main.py

Cada ejercicio es una función y también incluye:
if __name__ == "__main__":
    ejercicioN()

Al inicio de cada ejercicio se recarga datos.py para que los cambios realizados
por un ejercicio no se arrastren al siguiente cuando se ejecutan desde el menú.

He ajustado algunos detalles para que los ejercicios correspondan con sus enunciados:
- Ejercicio 8: calcula la media solo de personajes humanos.
- Ejercicio 11: añade el personaje a personajes_frieren (no a pokemons).
- Ejercicio 14: elimina realmente la afiliación de la lista.
- Ejercicio 15: comprueba la raza "Humano", como aparece en los datos.
