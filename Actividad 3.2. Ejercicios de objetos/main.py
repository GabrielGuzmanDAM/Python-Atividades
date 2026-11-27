from ejercicios import *

if __name__ == "__main__":

    print("-------------------")
    print("EJERCICIO 1")
    print("-------------------")
    # Crear dos jarras
    jarra1 = Jarra(500)
    jarra2 = Jarra(1000)

    print("Estado inicial:")
    print("-------------------")

    print("Jarra 1:" , jarra1)
    print("Jarra 2" , jarra2)

    # Llenar una jarra
    jarra1.llenar()
    jarra2.llenar()
    print("\nDespués de llenar la jarra 1 y 2:")
    print("-------------------")

    print(jarra1)
    print(jarra2)

    # Vaciar una jarra
    jarra2.vaciar()
    print("\nDespués de vaciar la jarra 2:")
    print("-------------------")

    print(jarra2)

    # Servir agua
    jarra1.servir(200)
    print("\nDespués de servir 200 litros:")
    print("-------------------")

    print(jarra1)

    # Pasar agua de una jarra a otra
    jarra2.llenar_desde(jarra1)
    print("\nDespués de llenar jarra 1 desde jarra 2:")
    print("-------------------")

    print(f"Jarra 1: {jarra1}")
    print(f"Jarra 2: {jarra2}")

    print("-------------------")
    print("EJERCICIO 2")
    print("-------------------")

    # Crear dos jarras
    puntoA = Punto(3,4)
    puntoB = Punto(3-3)

    segmento = Segmento(puntoA,puntoB)
    
        print("Estado inicial:")
        print("-------------------")
    
        print("Jarra 1:" , jarra1)
        print("Jarra 2" , jarra2)
    
        # Llenar una jarra
        jarra1.llenar()
        jarra2.llenar()
        print("\nDespués de llenar la jarra 1 y 2:")
        print("-------------------")
    
        print(jarra1)
        print(jarra2)
    
        # Vaciar una jarra
        jarra2.vaciar()
        print("\nDespués de vaciar la jarra 2:")
        print("-------------------")
    
        print(jarra2)
    
        # Servir agua
        jarra1.servir(200)
        print("\nDespués de servir 200 litros:")
        print("-------------------")
    
        print(jarra1)
    
        # Pasar agua de una jarra a otra
        jarra2.llenar_desde(jarra1)
        print("\nDespués de llenar jarra 1 desde jarra 2:")
        print("-------------------")
    
        print(f"Jarra 1: {jarra1}")
        print(f"Jarra 2: {jarra2}")

