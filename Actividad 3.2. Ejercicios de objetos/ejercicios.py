import math

#Ejercicio 1
class Jarra:
    def __init__(self, capacidad: int, contenido = 0):
        if capacidad < 1:
            raise ValueError("La capacidad no puede ser negativo")
        elif contenido < 0:
            raise ValueError("El contenedor no puede ser negativo")
        elif contenido > capacidad:
            contenido = capacidad
        
        self.capacidad = capacidad
        self.contenido = contenido

    def llenar(self):
        self.contenido = self.capacidad

    def vaciar(self):
        self.contenido = 0

    def llenar_desde(self, jarra: Jarra):
        cantidad = min(jarra.contenido, self.capacidad - self.contenido)
        self.contenido += cantidad
        jarra.contenido -= cantidad
    
    def servir(self, cantidad: int):
        self.contenido -= cantidad
        if self.contenido < 0:
            raise ValueError("No hay suficiente capasidad en la jarra")

    def __str__(self):
        return f"Capacidad: {self.capacidad} | Contenido: {self.contenido}"

#Ejercicio 2
class Punto:
    def __init__(self, coordenadaX: int = 0, coordenadaY: int = 0):
        if coordenadaX < -100 or coordenadaX > 100:
            raise ValueError("La cordenada X tiene que estar entre -100 y 100")
        elif coordenadaY < -100 or coordenadaY > 100:
            raise ValueError("La cordenada Y tiene que estar entre -100 y 100")

        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

    def __str__(self):
        return f"X: {self.coordenadaX} | Y: {self.coordenadaY}"

    def __eq__(self, otro: Punto):
        return self.capacidad == otro.capacidad and self.contenido == otro.contenido

class Segmento:
    def __init__(self, puntoA: Punto = {0,0}, puntoB: Punto = {1,1}):

        self.puntoA = puntoA
        self.puntoB = puntoB

    def __str__(self):
        return f"PuntaA: {self.puntoA} | PuntoB: {self.puntoB}"

    def longitud(self):
        return math.sqrt(math.pow(self.puntoB.coordenadaX - self.puntoA.coordenadaX, 2) + math.pow(self.puntoB.coordenadaY - self.puntoA.coordenadaY, 2))

    def __eq__(self, otro: Segmento):
        return self.puntoA == otro.puntoA and self.puntoB == otro.puntoB
        