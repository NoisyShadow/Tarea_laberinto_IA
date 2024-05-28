from laberinto import *
# Cargar y resolver el laberinto
archivo_laberinto = 'lab2.txt'
laberinto = Laberinto(archivo_laberinto)

# Imprimir el laberinto inicial
print("Laberinto inicial:")
laberinto.print_laberinto()

# Resolver el laberinto utilizando búsqueda en anchura (BFS)
encontrado = laberinto.solucion()

# Imprimir el laberinto con la solución (si se encontró)
if encontrado:
    print("Laberinto con la solución:")
    laberinto.print_laberinto()
else:
    print("No se encontró solución para el laberinto.")