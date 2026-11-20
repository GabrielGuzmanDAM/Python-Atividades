#----------------------------------
#EJERCICIO 01

def aplicar_funcion(numero : int , operacion : str) -> int:

    resultado = 0;

    str1 = "sumatorio";
    str2 = "factorial";

    if operacion == str1:
        resultado = sumatorio(numero)
    elif operacion == str2:
        resultado = factorial(numero)
    else :
        resultado = -2 

    return resultado

def sumatorio(numero : int) -> int:

    resultado = 0

    if numero >= 0:
        for i in range(numero, 0, -1):
            resultado += i;
    else :
        resultado = -1 

    return resultado

def factorial(numero : int) -> int:

    resultado = 0

    if numero >= 1:
        for i in range(numero, 1, -1):
            resultado *= i;
    else :
        resultado = -1 

    return resultado


#----------------------------------
#EJERCICIO 02

def comprobar_estado() -> bool:

    resultado = False

    print("----------------------------------")
    print("EJERCICIO 02")
    print("----------------------------------")

    return resultado

#----------------------------------
#EJERCICIO 03

def cambiar_divisa() -> bool:

    resultado = False

    print("----------------------------------")
    print("EJERCICIO 03")
    print("----------------------------------")

    return resultado