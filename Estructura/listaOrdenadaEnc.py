class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class ListaOrdenada:
    def __init__(self):
        self.cabeza = None
        self.cant = 0

    def insertar(self, elemento):
        nodo = Nodo(elemento)
        if self.cabeza is None or self.cabeza.elemento > elemento:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            aux = self.cabeza
            while aux is not None and aux.elemento < elemento:
                anterior = aux
                aux = aux.siguiente
            
            anterior.siguiente = nodo
            nodo.siguiente=aux
        self.cant+=1

    def suprimir(self, posicion):
        if 1 <= posicion <= self.cant:
            aux = self.cabeza
            anterior = None

            if posicion == 1:
                print(f"Eliminado: {aux.elemento}")
                self.cabeza = aux.siguiente

            else:
                i = 1
                while i < posicion:
                    anterior = aux
                    aux = aux.siguiente
                    i += 1
            
                if aux:
                    print(f"Eliminado: {aux.elemento}")
                    anterior.siguiente = aux.siguiente
            self.cant -= 1

lista=ListaOrdenada()
