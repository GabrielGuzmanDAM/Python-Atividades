# Variables
a = 2
b = 2.3
c = "HOLA"

d, f, q = 1, 2, 3
print(d, f, q)

print(a)
print (type(a)) # para saver la variable

a = "prueva"
print(a)
print (type(a))

# padir un numero, el input siempre pilla un string
print("Dame un dato:")
a = input()
print(a)

# nota
print("hola\nMundo") #\n para eparar un print en dos

# si queres ejecutar un script dede la consola SMD tienes que ponerte en el directorio donde tien es el script y escribe: "Python nombre_scipt.py"

# se pueden crear entornos: python -m venv entorno_ejemplo
# Se deve activar el entorno: .\entorno_ejemplo\Scripts\activate
# para crear un entprno con otra vercion de python: py -3.13.15 -m venv entorno_ejemplo2
# comando para ver la vercion de python: py --version
# python -m pip install --upgrade pip

#pip install django

# Listas: una susecion ordenadas de elementos que empiesan en 0 y se pueden camviar.
lista = [1,2,3]
print(lista)
print(lista[0])
lista[1] = -2

lista.append(4)
print(list)

lista.extend(4,5,6)
print(list)

lista2 = [1,2,3]

lista.extend(lista2)
print(list)

lista.remove(3) #elimina el primer 3 que encuentre

del lista[0] #bora la pocicion 0

# ejemplo:
producto = [1,"TV 40", 199.92, "LG"]
print(producto)

# tubla: es como una lizta pero no e puede cambiar sus variables o agregar variables
tupla = (1,2,3)
print(tupla)
print(tupla[0])

# rango: una susecion de numeros ordenados, en este ejemplo todos los numeros entre 1 y 10, si pones un dos es para que el dos no te pueda salir
rango = range(1,10)
print(rango)
print(rango[3])

inicio = int(input("Inicio:"))
fin = int(input("fin:"))
rango = range(inicio,fin)

# len: puedes ver la longitud de cualquier conjunto de variables
print(len(rango))