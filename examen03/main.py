from practica31 import convertir_acciones

if __name__ == "__main__":

    ejercicio01 = convertir_acciones("nvda", 10, "euro")
    ejercicio02 = convertir_acciones("sony", 5, "dolar")
    ejercicio03 = convertir_acciones("bmw", 20, "libra")
    ejercicio04 = convertir_acciones("ssss", 20, "sss")

    print(f"resultado: {ejercicio01}")
    print(f"resultado: {ejercicio02}")
    print(f"resultado: {ejercicio03}")
    print(f"resultado: {ejercicio04}")