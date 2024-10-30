class Nodo:
    dato:int
    izq:object
    der:object
    
    def __init__(self,dato):
        self.dato=dato
        self.izq= None
        self.der= None

class ArbolBB:
    raiz:Nodo

    def __init__(self):
        self.raiz= None

    def insertar(self,subarbol,clave):
        if  self.raiz is None:
            nodo = Nodo(clave)
            self.raiz = nodo
        else:
            if clave < subarbol.dato:
                if subarbol.izq is None:
                    nodo= Nodo(clave)
                    subarbol.izq = nodo
                else:
                    self.insertar(subarbol.izq, clave)
            elif clave > subarbol.dato:
                if subarbol.der is None:
                    nodo = Nodo(clave)
                    subarbol.der = nodo
                else:
                    self.insertar(subarbol.der, clave)
            else:
                print("Ya existe clave")

    def buscar(self,subarbol,clave):
        if subarbol is None:
            #print("No está")
            return None
        else:
            if clave == subarbol.dato:
                return subarbol
            elif clave > subarbol.dato:
                 return self.buscar(subarbol.der, clave)
            else:
                return self.buscar(subarbol.izq, clave)
        
    def hoja(self,clave):
        nodo = self.buscar(self.raiz, clave)
        return nodo is not None and nodo.izq is None and nodo.der is None

    def hijo(self,padre,hijo):
        nodoPadre = self.buscar(self.raiz,padre)
        nodoHijo = self.buscar(self.raiz,hijo)
        hijo = False
        if nodoHijo is not None and nodoPadre is not None:
            hijo = nodoPadre.izq==nodoHijo or nodoPadre.der==nodoHijo
        return hijo
    
    def nivel(self, subarbol, clave, nivel=0):
        if subarbol is None:
            return -1
        if clave == subarbol.dato:
            return nivel
        elif clave < subarbol.dato:
            return self.nivel(subarbol.izq, clave, nivel + 1)
        else:
            return self.nivel(subarbol.der, clave, nivel + 1)
        
    def contarDescendientes(self, nodo):
        if nodo is None:
            return 0
        return self.contarDescendientes(nodo.izq) + self.contarDescendientes(nodo.der) + 1

    def imprimirHojas(self, nodo):
        if nodo is not None:
            if nodo.izq is None and nodo.der is None:
                print(nodo.dato)
            else:
                self.imprimirHojas(nodo.izq)
                self.imprimirHojas(nodo.der)

    def contarNodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contarNodos(nodo.izq) + self.contarNodos(nodo.der)

    def InOrder(self,subarbol):
        if subarbol:
            self.InOrder(subarbol.izq)
            print(subarbol.dato)
            self.InOrder(subarbol.der)

if __name__=='__main__':
    arbol=ArbolBB()
    arbol.insertar(arbol.raiz,9)
    arbol.insertar(arbol.raiz,5)
    arbol.insertar(arbol.raiz,10)
    arbol.InOrder(arbol.raiz)
    nodo=(arbol.buscar(arbol.raiz, 10))
    print(nodo.dato)
    if arbol.hoja(5):
        print("Es hoja")
    else:
        print("No es hoja")

    if arbol.hijo(9, 5):
        print("Es hijo")
    else:
        print("No es hijo")

    print(arbol.nivel(arbol.raiz, 10))

    nodo = arbol.buscar(arbol.raiz, 9)
    if nodo:
        print(f"El nodo con clave {9} tiene {arbol.contarDescendientes(nodo)-1} descendientes.")
    arbol.imprimirHojas(arbol.raiz)
    print(arbol.contarNodos(arbol.raiz))
