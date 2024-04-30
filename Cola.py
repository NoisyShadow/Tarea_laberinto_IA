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

    def encolar(self,value):
        nuevonodo = nodo(value)
        if self.Vacio():
            self.cabeza = nuevonodo
            self.final = nuevonodo
        else:
            self.final.siguiente = nuevonodo
            self.final = nuevonodo
        return True
    
    def desencolar (self):# Elimina y devuelve el primer elemento de la cola
        if self.Vacio(): 
            return None
        valor_desencolado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        return valor_desencolado 

  
#Testing cola
i = Cola()
i.encolar(1)
i.encolar(2)
i.encolar(5)

print(i.desencolar())
print(i.desencolar())
print(i.desencolar())