class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza=None
        self.cant=0

    def insertar(self, posicion, elemento):
        if 1 <= posicion <= self.cant+1:
            nodo=Nodo(elemento)
            if posicion == 1:
                nodo.siguiente=self.cabeza
                self.cabeza=nodo
            else:
                aux=self.cabeza
                i=1
                while i<posicion-1:
                    aux=aux.siguiente
                    i+=1
                nodo.siguiente=aux.siguiente
                aux.siguiente=nodo
            self.cant+=1
        else:
            print("Error")

    def suprimir(self, posicion):
        if 1 <= posicion <= self.cant:
            aux = self.cabeza
            anterior = None

            if posicion == 1:
                print(f"Eliminado: {aux.elemento}")
                self.cabeza = aux.siguiente
            else:
                i=1
                while i < posicion:
                    anterior = aux
                    aux = aux.siguiente
                    i += 1
            
                if aux:
                    anterior.siguiente = aux.siguiente
                    aux.siguiente = None
                    print(f"Eliminado: {aux.elemento}")
                    self.cant -= 1
        else:
            print("Error")


    def recorrer(self):
        aux = self.cabeza
        while aux!=None:
            print(aux.elemento)
            aux = aux.siguiente

lista=Lista()





            
