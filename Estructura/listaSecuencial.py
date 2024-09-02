class ListaSec:
    def __init__(self, max):
        self.max = max
        self.elementos = [None] * max
        self.ult = -1

    def insertar(self, posicion, elemento):
        if 1 <= posicion <= self.ult+2 and self.ult < self.max-1:
            for i in range(self.ult, posicion-2, -1):
                self.elementos[i + 1] = self.elementos[i]
            self.elementos[posicion - 1] = elemento
            self.ult += 1
        else:
            print("Error")

    def suprimir(self, posicion):
        if 1 <= posicion <= self.ult+1:
            eliminado=self.elementos[posicion-1]
            for i in range(posicion-1, self.ult):
                self.elementos[i]=self.elementos[i+1]
            self.ult -= 1
            return eliminado
        else:
            print("Error")
        
    def recuperar(self, posicion):
        if 1 <= posicion <= self.ult:
            return self.elementos[posicion-1]
        else:
            print("Error")

    def localizar(self, elemento):
        i=0
        while i < self.ult:
            if self.elementos[i]==elemento:
                return i
            i+=1
        print("Error")

    def primerElemento(self):
        if self.ult>0:
            return self.elementos[0]
        else:
            print("Error")

    def ultimoElemento(self):
        if self.ult>0:
            return self.elementos[self.ult]
        else:
            print("Error")

    def recorrer(self):
        if self.ult>=0:
            for i in range(self.ult+1):
                print(self.elementos[i])


            
        