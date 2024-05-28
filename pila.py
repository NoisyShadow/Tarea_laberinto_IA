
class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila():
    def __init__(self, ):
        self.cima = None
    
    def Vacio(self):
        return self.cima is None
    
    def agregar(self, valor):
        nuevonodo = nodo(valor)
        nuevonodo.siguiente = self.cima
        self.cima = nuevonodo

    def eliminar(self):
        if self.Vacio(): 
            return None
        valor_desapilado = self.cima.dato
        self.cima = self.cima.siguiente
        return valor_desapilado


#
#i = pila()
#i.agregar(1)
#i.agregar(2)
#i.agregar(5)

#print(i.desagregar())
#print(i.desagregar())
#print(i.desagregar())