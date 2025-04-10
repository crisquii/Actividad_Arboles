class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.ramas = Lista()

class Lista:
    def __init__(self):
        self.cabeza = None
        
    def insertarDespuesX(self, dato1, dato2):
        if self.cabeza == None:
            return False
        else:
            control = self.cabeza
            while(control != None):
                insertarDespuesX
                   
class Arbol:
    def __init__(self, data):
        self.arbol = Lista()
        self.arbol.insertarInicio(data)
        
    def agregarNodo(self, data1, data2):
        nuevo_nodo = Nodo(dato1)
        self.arbol.cabeza.ramas.insertarDespues(data1, data2) 