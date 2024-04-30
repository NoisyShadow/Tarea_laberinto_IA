
class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class pila:
    def __init__(self, ):
        self.cima = None
    
    def Vacio(self):
        return self.cima is None
    
    def apilar(self, valor):
        nuevonodo = nodo(valor)
        nuevonodo.siguiente = self.cima
        self.cima = nuevonodo

    def desapilar(self):
        if self.Vacio(): 
            return None
        valor_desapilado = self.cima.dato
        self.cima = self.cima.siguiente
        return valor_desapilado



i = pila()
i.apilar(1)
i.apilar(2)
i.apilar(5)

print(i.desapilar())
print(i.desapilar())
print(i.desapilar())