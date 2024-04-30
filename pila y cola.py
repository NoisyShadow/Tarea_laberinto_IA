#integrante: Ilan Camilo Vargas Bahamonde
#Primera entrega tarea IA

class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #


class Cola():
    def __init__(self):#Inicializa la cola vacia
        self.cabeza = None 
        self.final = None 

    def Vacio(self):#Se encarga de verificar que la pila este vacia
        return self.cabeza is None and self.final is None

    def encolar(self,value):#Añade un elemento al final de la cola
        nuevonodo = nodo(value)#Se crea un nuevo nodo con el valor ingresado
        if self.Vacio():#En caso de estar vacia la cola, el nodo se coniverte en la cabeza y el final de la cola a la vez
            self.cabeza = nuevonodo
            self.final = nuevonodo
        else:#En caso contrario el nuevo nodo se enlaza al final de la de la cola y se actualiza la cola
            self.final.siguiente = nuevonodo
            self.final = nuevonodo
        return True
    
    def desencolar (self):# Elimina y devuelve el primer elemento de la cola
        if self.Vacio(): #Si la cola esta vacia no se puede desencolar ningun valor o nodo
            return None
        valor_desencolado = self.cabeza.dato #Obtiene el dato de la cabeza de la cola
        self.cabeza = self.cabeza.siguiente#Actualiza el valor de la pila con el siguiente valor o nodo
        if self.cabeza is None: #si la cola esta vacia despues de desencolar, se actualiza el final de esta tambien.
            self.final = None
        return valor_desencolado 

  
#Testing cola.
i = Cola()
i.encolar(1)
i.encolar(2)
i.encolar(5)
#Se mostraran los resultados de desencolar.
print("cola desencolada")
print(i.desencolar())
print(i.desencolar())
print(i.desencolar())

#
class pila:
    def __init__(self, ):
        self.cima = None#Se inicializa una pila vacia.
    
    def Vacio(self):#Verficia si la pila esta vacia.
        return self.cima is None
    
    def apilar(self, valor):#Función encargada de agregar un nuevo elemento a la cima de la pila.
        nuevonodo = nodo(valor) #Se crea un nuevo nodo con el valor ingresado
        nuevonodo.siguiente = self.cima #El nuevo nodo 
        self.cima = nuevonodo#Se actualiza la cima de la pila con el nuevo nodo

    def desapilar(self):
        if self.Vacio(): #Si la pila esta vacia no se puede desencolar ningun valor o nodo
            return None
        valor_desapilado = self.cima.dato#Obtiene el dato de la cima en la pila
        self.cima = self.cima.siguiente#Actualiza el valor de la pila con el siguiente valor o nodo
        return valor_desapilado


#testing de la pila.
i = pila()
i.apilar(1)
i.apilar(2)
i.apilar(5)
#Se mostraran los resultados de desapilar.
print("pila desapilada")
print(i.desapilar())
print(i.desapilar())
print(i.desapilar())