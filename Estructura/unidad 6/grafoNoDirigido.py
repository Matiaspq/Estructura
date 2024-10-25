from colasecuencial import Cola

class GrafoNoDirigido:
    def __init__(self, nodos):
        self.matriz = [[0 for _ in range(nodos)] for _ in range(nodos)]
        """[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]"""
    
    def arista(self, i, j):
        # No dirigido, se conecta en ambos sentidos
        self.matriz[i][j] = 1
        self.matriz[j][i] = 1

    def adyacente(self, origen):
        adyacente=[]
        for j in range(len(self.matriz)):
            if self.matriz[origen][j]==1:
                adyacente.append(j)
        return adyacente

    def conexo(self):
        j=0
        for i in range(len(self.matriz)):
            print(f"i{i}")
            aux=self.bea(i)
            while aux[j-1]!=999 and j<len(aux):
                print(f"aux:{aux[j]}")
                print(f"j{j}")
                j+=1



    def bea(self, origen):
        cola=Cola(50)
        d = [999]*5
        print(d)
        d[origen] = 0
        cola.insertar(origen)
        while not cola.vacia():
            eliminado=cola.eliminar()
            aux=self.adyacente(eliminado)
            for i in aux:
                if d[i]==999:
                    d[i] = d[eliminado]+1
                    cola.insertar(i)
        return d


    def mostrar(self):
        for fila in self.matriz:
            print(fila)

if __name__=='__main__':
    grafo=GrafoNoDirigido(5)
    grafo.arista(1,2)
    grafo.arista(3,2)
    grafo.arista(4,3)
    grafo.mostrar()
    grafo.adyacente(0)
    grafo.bea(1)
    print("--------------")
    grafo.conexo()


    

