class ListaOrdSec:
    def __init__(self, max):
        self.max = max
        self.elementos = [None] * max
        self.cant = 0

    def insertar(self, elemento):
        if self.cant < self.max:
            posicion = 0
            while posicion < self.cant and self.elementos[posicion] < elemento:
                posicion += 1
            
            for i in range(self.cant, posicion, -1):
                self.elementos[i] = self.elementos[i - 1]
            
            self.elementos[posicion] = elemento
            self.cant += 1
        else:
            print("Error")

    def suprimir(self, posicion):
        if 1 <= posicion <= self.cant:
            eliminado = self.elementos[posicion-1]
    
            for i in range(posicion-1, self.cant - 1):
                self.elementos[i] = self.elementos[i + 1]
            self.cant -= 1
            print(eliminado)

        else:
            print("Error")

    def recorrer(self):
        if self.cant>=0:
            for i in range(self.cant):
                print(self.elementos[i])

lista = ListaOrdSec(10)
