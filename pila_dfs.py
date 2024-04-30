#pila modificada para funcionar con el metodo DFS
class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #

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