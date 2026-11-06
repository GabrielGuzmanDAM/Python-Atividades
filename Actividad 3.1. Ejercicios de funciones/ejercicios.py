# 1. Crea una función llamada comprobarLetraDNI que reciba una cadena de
# caracteres que representará al DNI de una persona y devuelva True si el DNI
# es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros
# seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
# conocer si la letra es correcta puedes consultar la web del Ministerio del
# Interior.

def comprobarLetraDNI(dni: str) -> bool:

    resultado = False

    print("----------------------------------")
    print("EJERCICIO 01")
    print("----------------------------------")

    # len(str)        -> Devuelve la longitud de una cadena o lista.
    # .isdigit()    -> Comprueba si una cadena contiene únicamente números.
    # .isalpha()    -> Comprueba si una cadena contiene únicamente letras.
    # int(str)        -> Convierte un valor a número entero.
    # .upper()      -> Convierte una cadena a mayúsculas.
    # .lower()      -> Convierte una cadena a minúsculas.
    # %            -> Devuelve el resto de una división (módulo).
    # []           -> Permite acceder a un carácter mediante su índice.
    # [:-1]        -> Obtiene todos los caracteres excepto el último.
    # [-1]         -> Obtiene el último carácter.
    if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
        numero = int(dni[:-1])
        letra = dni[-1].upper()
        letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra_correcta = letras_validas[numero % 23]
        if letra == letra_correcta:
            resultado = True


    return resultado

# 2. Crea una función llamada convertirTemperatura que reciba un número con
# decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
# serán “C”, “K” y “F”, que representan unidades de temperatura (Celsius,
# Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
# resultado de convertir de la primera unidad que reciba la función a la
# segunda. Por ejemplo, convertirTemperatura(10,”F”,”C”) devolvería el
# resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos
# decimales, redondeando al valor más cercano.

def convertirTemperatura(num: float, unidad1: str, unidad2: str) -> float:

    resultado = 0.0

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    # round(float, int) -> Redondea un número a un número específico de decimales.

    if unidad1 == "C":
        if unidad2 == "K":
            resultado = num + 273.15
        elif unidad2 == "F":
            resultado = (num * 9/5) + 32
    elif unidad1 == "K":
        if unidad2 == "C":
            resultado = num - 273.15
        elif unidad2 == "F":
            resultado = ((num - 273.15) * 9/5) + 32
    elif unidad1 == "F":
        if unidad2 == "C":
            resultado = (num - 32) * 5/9
        elif unidad2 == "K":
            resultado = ((num - 32) * 5/9) + 273.15
    else:
        print("Unidades de temperatura no válidas.")

    return round(resultado, 2)

# 3. Crea una función llamada calcularValorBruto, que reciba un número con
# decimales (el precio de un producto) y una cadena de caracteres (que
# representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
# serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
# resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
# calcularValorBruto(10,”GENERAL”) devolvería el resultado de sumar a los
# 10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
# que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
# hacia arriba.

def calcularValorBruto(precio: float, tipo_iva: str) -> float:

    resultado = 0.0
    sumaImpuestos = 0.0

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    if tipo_iva == "GENERAL":
        sumaImpuestos = precio * 0.21
    elif tipo_iva == "REDUCIDO":
        sumaImpuestos = precio * 0.10
    elif tipo_iva == "SUPERREDUCIDO":
        sumaImpuestos = precio * 0.04
    else:
        print("Tipo de IVA no válido")

    resultado = precio + sumaImpuestos

    return round(resultado, 2)