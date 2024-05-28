class Nodo:
    def __init__(self, dato):
        self.dato = dato #Almacena el valor del nodo
        self.siguiente = None #Funcion que referencia al siguiente nodo 

class Cola:
    def __init__(self): #Inicializa la cola vacia
        self.cabeza = None #Referencia al primer nodo de la cola
        self.final = None #Referencia al último nodo de la cola
        self.tamanho_cola = 0 #Tamaño de la cola

    def vacio(self): #Se encarga de verificar que la pila este vacia
        return self.cabeza is None and self.final is None

    def agregar(self, valor): #Añade un elemento al final de la cola
        nuevo_nodo = Nodo(valor) #Se crea un nuevo nodo con el valor ingresado
        if self.vacio(): #En caso de estar vacia la cola, la cabeza y final apuntan al nuevo nodo
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else: #Si no esta vacía, agrega el nuevo nodo al final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamanho_cola += 1 #Incrementa el tamaño de la cola
        return True
    
    def eliminar(self): #Elimina y devuelve el primer elemento de la cola
        if self.vacio():
            return None #Si la cola esta vacia no se puede eliminar ningun valor
        valor_eliminado = self.cabeza.dato #Obtiene el valor del nodo que se va a eliminar
        self.cabeza = self.cabeza.siguiente #Actualiza el valor de la pila con el siguiente valor o nodo
        self.tamanho_cola -= 1 #Disminuye el tamaño de la cola
        if self.cabeza is None: #Si la cabeza es None, la cola está vacía, y final debe ser None también
            self.final = None
        return valor_eliminado #Devuelve el valor en la cabeza de la cola
    
    def retornar(self):
        if self.vacio():
            return None #En caso de estar vacía no se puede retornar 
        return self.cabeza.dato #Devuelve el valor en la cabeza de la cola
    
    def tamanho(self):
        #Devuelve el tamaño de la cola
        return self.tamanho_cola

class Pila:
    def __init__(self):
        self.cabeza = None #Referencia al primer nodo de la pila
        self.tamanho_pila = 0 #Tamaño de la pila
    
    def vacio(self): #Verficia si la pila esta vacia.
        return self.cabeza is None
    
    def agregar(self, valor): #Función encargada de agregar un nuevo elemento a la cima de la pila.
        nuevo_nodo = Nodo(valor) #Se crea un nuevo nodo con el valor ingresado
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo #Se actualiza la cabeza de la pila con el nuevo nodo
        self.tamanho_pila += 1

    def eliminar(self):
        if self.vacio(): #Si la pila esta vacia no se puede desencolar ningun valor o nodo
            return None
        valor_eliminado = self.cabeza.dato #Obtiene el dato de la cima en la pila
        self.cabeza = self.cabeza.siguiente #Actualiza el valor de la pila con el siguiente valor o nodo
        self.tamanho_pila -= 1
        return valor_eliminado #Devuelve el valor en la cabeza de la pila
        
    def retornar(self):
        if self.vacio():
            return None
        return self.cabeza.dato
    
    def tamanho(self):
        return self.tamanho_pila

class Laberinto:
    def __init__(self, archivo):
        with open(archivo) as f:
            contenido = f.read()#Lee el contenido del archivo

        lineas = contenido.split('\n') #Divide el contenido en líneas
        self.altura = self.contar_lineas(lineas) #Calcula la altura del laberinto
        self.ancho = self.obtener_ancho(lineas) #Calcula el ancho del laberinto
        self.solucion = Pila()  # Usar Pila para almacenar la solución
        self.paredes = Pila() #Usa una Pila para almacenar las paredes
        self.inicio = None #Coordenadas del punto de inicio
        self.meta = None #Coordenadas del punto de meta
        self.padres = {} #diccionario para rastrear a los padres de cada nodo
        self.paredes_set = set()  # Conjunto para almacenar las posiciones de las paredes

        for i, linea in enumerate(lineas):
            for j, caracter in enumerate(linea):
                if caracter == "A":
                    self.inicio = (i, j) #Establece el punto de inicio
                elif caracter == "B":
                    self.meta = (i, j) #Establece el punto meta
                elif caracter == "#":
                    pared = (i, j) #Establece una pared
                    self.paredes.agregar(pared)
                    self.paredes_set.add(pared)  # Agregar la posición de la pared al conjunto

    def contar_lineas(self, lineas):
        contador = 0
        for linea in lineas:
            if linea.strip():
                contador += 1 #Incrementa el contador por cada linea no vacía
        return contador #Devuelve el número de lineas

    def obtener_ancho(self, lineas):
        ancho_max = 0
        for linea in lineas:
            ancho_actual = 0
            for caracter in linea:
                if caracter != '\n':
                    ancho_actual += 1 #Incrementa el ancho actual
            if ancho_actual > ancho_max: #Actualiza el ancho máximo si el actual es mayor
                ancho_max = ancho_actual
        return ancho_max
    
    def print_laberinto(self):
        for i in range(self.altura):
            for j in range(self.ancho):
                if (i, j) == self.inicio:
                    print("A", end="")
                elif (i, j) == self.meta:
                    print("B", end="")
                elif not self.revisar_pared((i, j)):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def print_recorrido(self):
        if not self.solucion.vacio():
            solucion_elementos = self.obtener_elementos_solucion()
            for i in range(self.altura):
                for j in range(self.ancho):
                    if (i, j) == self.inicio:
                        print("A", end="")
                    elif (i, j) == self.meta:
                        print("B", end="")
                    elif (i, j) in solucion_elementos:
                        print("*", end="")
                    elif not self.revisar_pared((i, j)):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        else:
            print("No se encontró una solución para el laberinto.")

    def obtener_elementos_solucion(self):
        elementos = set() #Conjunto para los Elementos de la solución
        pila_aux = Pila() #Pila auxiliar utilizada ´para almacenar de manera temporal los elementos de la solución
        while not self.solucion.vacio():
            elemento = self.solucion.eliminar() #Elimina el elemento de la solucion
            elementos.add(elemento) #Agrega el elemento al conjunto
            pila_aux.agregar(elemento) #Agrega el elemento a la pila auxiliar
        while not pila_aux.vacio():
            self.solucion.agregar(pila_aux.eliminar()) #Restaura los elementos en la pila de la solucion
        return elementos

    def revisar_pared(self, dato):
        nodo_actual = self.paredes.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                return True #Devuelve un True si encuentra una pared en la posición
            nodo_actual = nodo_actual.siguiente
        return False #Devuelve False si no se encontro una pared

    def revisar_frontera(self, dato, frontera):
        nodo_actual = frontera.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                return True #Devuelve True si encuentra el dato en la frontera
            nodo_actual = nodo_actual.siguiente
        return False #Devuelve False si no encuentra el dato en la frontera

    def vecinos(self, state):
        fila, columna = state
        opciones = [
            ((fila - 1, columna)),  # Movimiento hacia arriba
            ((fila + 1, columna)),  # Movimiento hacia abajo
            ((fila, columna - 1)),  # Movimiento hacia la izquierda
            ((fila, columna + 1))   # Movimiento hacia la derecha
        ]
        
        vecinos_validos = Pila() #Uso de pila para almacenar vecinos válidos
        for (f, c) in opciones:
            if 0 <= f < self.altura and 0 <= c < self.ancho and not self.revisar_pared((f, c)):
                vecinos_validos.agregar((f, c)) #Agrega el vecino si es válido
        return vecinos_validos #Devuelve lapila de vecinos válidos

    def resolver(self):
        frontera = Pila() #Segun se use pila sera metodo DFS
                        #En caso de usar Cola sera metodo BFS
        explorado = set() #Conjunto para almacenar estados explorados
        frontera.agregar(self.inicio) #Agrega el estado al conjunto de explorados

        while not frontera.vacio():
            current_state = frontera.eliminar()
            explorado.add(current_state)

            if current_state == self.meta:
                #En caso de encontrar la meta, se construye el camino de solución
                self.solucion.agregar(current_state)
                while current_state != self.inicio:
                    current_state = self.padres[current_state]
                    self.solucion.agregar(current_state)
                return True #Devuelve True si se encuentra una solución

            vecinos = self.vecinos(current_state)
            while not vecinos.vacio():
                estado_vecino = vecinos.eliminar()  #Elimina un vecino de la pila de vecinos
                if estado_vecino not in explorado and not self.revisar_frontera(estado_vecino, frontera):
                    frontera.agregar(estado_vecino) #Agrega el vecino a la frontera si no ha sido explorado
                    # Guardar el padre del estado vecino para reconstruir el camino después
                    self.padres[estado_vecino] = current_state

        return False #Devuelve False si no se encuentra una solución

laberinto = Laberinto("lab1.txt")
#laberinto = Laberinto("lab2.txt")
#laberinto = Laberinto("lab3.txt")
#laberinto = Laberinto("lab4.txt")
#LAB 4 SIN SOLUCION
laberinto.print_laberinto()

if laberinto.resolver():
    print("¡Se encontró una solución para el laberinto!")
    laberinto.print_recorrido()
else:
    print("No se encontró una solución para el laberinto.")
