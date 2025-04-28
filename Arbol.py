class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.ramas = Lista()

    def agregarRama(self,dataX,data):
        if self.data == data:
            self.ramas.insertarLista(dataX)
            return True
        else:
            control = self.ramas.cabeza
            while control != None:
                if control.agregarRama(dataX, data):
                    return True
                control = control.siguiente
            return False
        
    def contarNodos(self, contador):
        contador = contador + 1
        control = self.ramas.cabeza
        while control != None:
                contador = control.contarNodos(contador)
                control = control.siguiente
        return contador
     
    def sacarOrden(self, contador):
        if contador < self.ramas.contar():
            contador = self.ramas.contar()
        control = self.ramas.cabeza
        while control != None:
                contador = control.sacarOrden(contador)
                control = control.siguiente
        return contador 

    def sacarAltura(self, contador):
        contador = contador + 1
        altura = contador
        control = self.ramas.cabeza
        while control != None:
                if altura < control.sacarAltura(contador):
                    altura =  control.sacarAltura(contador)
                control = control.siguiente
        return altura 

class Lista:
    def __init__(self):
        self.cabeza = None

    def insertarLista(self, datoX):
        if self.cabeza == None:
            self.cabeza = Nodo(datoX)
        else:
            control = self.cabeza
            while control.siguiente != None:
                control = control.siguiente
            control.siguiente = Nodo(datoX)

    def contar(self):
        contador = 0
        control = self.cabeza
        while control != None:
                contador = contador + 1
                control = control.siguiente
        return contador
                   
class Arbol:
    def __init__(self, data):
        self.raiz = Nodo(data)
        
    def agregarNodo(self, dataX, data):
        if self.raiz.agregarRama(dataX,data):
            print("El nodo se agrego exitosamente.")
        else:
            print("Nose encontro el nodo suministrado.")

    def peso(self):
        contador = 0
        print(f"El peso del arbol es: {self.raiz.contarNodos(contador)}")

    def orden(self):
        contador = 0
        print(f"El orden del arbol es de: {self.raiz.sacarOrden(contador)}")

    def altura(self):
        contador = 0
        print(f"La altura del arbol es: {self.raiz.sacarAltura(contador)}")



arbol_1 = Arbol("hijo")
arbol_1.agregarNodo("papa", "hijo")
arbol_1.agregarNodo("mama", "hijo")
arbol_1.agregarNodo("madrastra", "hijo")
arbol_1.agregarNodo("abuela", "mama")
arbol_1.peso()
arbol_1.orden()
arbol_1.altura()