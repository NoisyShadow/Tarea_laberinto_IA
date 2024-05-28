class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #

class Cola():
    def __init__(self):
        self.cabeza = None #inicializa la cola vacia
        self.final = None

    def Vacio(self):#Se encarga de verificar que la pila este vacia
        return self.cabeza is None and self.final is None

    def agregar(self,value):
        nuevonodo = nodo(value)
        if self.Vacio():
            self.cabeza = nuevonodo
            self.final = nuevonodo
        else:
            self.final.siguiente = nuevonodo
            self.final = nuevonodo
        return True
    
    def eliminar (self):# Elimina y devuelve el primer elemento de la cola
        if self.Vacio(): 
            return None
        valor_desencolado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        return valor_desencolado 

  
#Testing cola.
#i = Cola()
#i.agregar(1)
#i.agregar(2)
#i.agregar(5)
#Se mostraran los resultados de eliminar.
#print("cola desencolada")
#print(i.eliminar())
#print(i.eliminar())
#print(i.eliminar())