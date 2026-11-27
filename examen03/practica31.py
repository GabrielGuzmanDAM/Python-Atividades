def convertir_acciones(empresa: str, acciones: int, moneda: str) -> float:

    precioAcciones = 0

    empresa = empresa.upper()
    moneda = moneda.upper()

    valorAccion = 0

    if empresa == "NVDA":
        valorAccion = 156.20
    elif empresa == "SONY":
        valorAccion = 24.16
    elif empresa == "BMW":
        valorAccion = 58.12

    valorAcciones = valorAccion * acciones

    if moneda == "EURO":
        precioAcciones = valorAcciones
    elif moneda == "DOLAR":
        precioAcciones = valorAcciones * 1.10
    elif moneda == "LIBRA":
        precioAcciones = valorAcciones * 0.83

    return round(precioAcciones, 2)
