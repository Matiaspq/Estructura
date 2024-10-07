import random

class Celda:
    def __init__(self, item=0, sig=None):
        self.item = item 
        self.sig = sig
    

class Pila:
    def __init__(self, xtope=None):
        self.tope = xtope

    def insertar(self, x):
        nuevo = Celda(x, self.tope)
        self.tope = nuevo

    def recorrer(self):
        aux = self.tope
        while aux!=None:
            print(aux.item)
            aux = aux.sig


class TablaHashEncadenado:
    def __init__(self, tamaño):
        self.tamaño=tamaño
        self.tabla=[Pila() for _ in range(tamaño)]

    def hashDivision(self, clave):
        return clave % self.tamaño

    def insertar(self, valor):
        i = self.hashDivision(valor)
        print(f"Indice: {i}")
        self.tabla[i].insertar(valor)

    def mostrar(self): #No pertenece a estructura
        for i in range(11):
            print(f"mostrar Indice {i}")
            print(self.tabla[i].recorrer())
       

    
if __name__=='__main__':
    tabla=TablaHashEncadenado(11)
    numeros=[]
    for i in range(10):
        aleatorio=random.randint(0,1000)
        numeros.append(aleatorio)
    print(numeros)
    for i in numeros:
        tabla.insertar(i)
    tabla.mostrar()

