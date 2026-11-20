from ejercicios import *

if __name__ == "__main__":

    while True:

        numero = int(input("Introduce un número: "))
        operacion = str(input("Introduce una operación: "))
        ejercicio01 = aplicar_funcion( numero , operacion)

        if ejercicio01 == -1:
            print(f"El valor no puede ser menor a 0 en sumando o menor a 1 en funcion")
            
        elif ejercicio01 == -2:
            print(f"La operacion no es valida (sumatorio o factorial)")

        else:
            print(f"------------------------------")
            print(f"prueva: {ejercicio01}")

            break

        

    
