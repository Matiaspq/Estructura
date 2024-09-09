class Celda:
    def __init__(self, item=None):
        self.item = item
        self.sig = None

class Cola:
    def __init__(self):
        self.pr = None  # puntero al primer nodo
        self.ul = None  # puntero al último nodo
        self.cant = 0   # cantidad de elementos en la cola

    def vacia(self):
        return self.cant == 0

    def insertar(self, x):
        nuevo_nodo = Celda(x)
        if self.ul is None:
            self.pr = nuevo_nodo
        else:
            self.ul.sig = nuevo_nodo
        self.ul = nuevo_nodo
        self.cant += 1
        return self.ul.item

    def suprimir(self):
        if self.vacia():
            return None  # Indicamos que la cola está vacía
        valor = self.pr.item
        self.pr = self.pr.sig
        if self.pr is None:
            self.ul = None
        self.cant -= 1
        return valor

    def recuperapr(self):
        return self.pr

    def recorrer_iterativo(self):
        nodo_actual = self.pr
        while nodo_actual is not None:
            print(nodo_actual.item)
            nodo_actual = nodo_actual.sig

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()

    print("Insertar 10:", cola.insertar(10))
    print("Insertar 20:", cola.insertar(20))
    print("Insertar 30:", cola.insertar(30))

    print("Contenido de la cola (recorrido iterativo):")
    cola.recorrer_iterativo()
    
    print("Suprimir:", cola.suprimir())
    print("Suprimir:", cola.suprimir())
    
    print("Contenido restante de la cola (recorrido iterativo):")
    cola.recorrer_iterativo()
