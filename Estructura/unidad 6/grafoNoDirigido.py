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

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

if __name__=='__main__':
    grafo=GrafoNoDirigido(5)
    grafo.arista(0,1)
    grafo.arista(1,2)
    grafo.arista(3,2)
    grafo.arista(4,3)
    grafo.mostrar()
    
