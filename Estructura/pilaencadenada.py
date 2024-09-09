class Celda:
    def __init__(self, item=0, sig=None):
        self.item = item  # Valor del nodo
        self.sig = sig    # Puntero al siguiente nodo


class Pila:
    def __init__(self, xtope=None, xcant=0):
        self.tope = xtope
        self.cant = xcant

    def vacia(self):
        return self.cant == 0

    def insertar(self, x):
        ps1 = Celda(x, self.tope)
        self.tope = ps1
        self.cant += 1
        return ps1.item

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return None
        else:
            x = self.tope.item
            self.tope = self.tope.sig
            self.cant -= 1
            return x

    def muestratope(self):
        if not self.vacia():
            return self.tope.item
        else:
            print("Pila vacía")
            return None

    def recuperatope(self):
        return self.tope


# Ejemplo de uso
p = Pila()
p.insertar(10)
p.insertar(20)
print(p.muestratope())  # Output: 20
print(p.suprimir())     # Output: 20
print(p.muestratope())  # Output: 10
