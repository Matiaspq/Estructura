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
        self.tiempo = 0
    
    def arista(self, i, j, peso):
        # No dirigido, se conecta en ambos sentidos
        self.matriz[i][j] = peso
        #self.matriz[j][i] = peso es dirigido

    def adyacente(self, origen):
        adyacente=[]
        for j in range(len(self.matriz)):
            if self.matriz[origen][j] != 0:
                adyacente.append(j)
        return adyacente

    def conexo(self):
        aux=self.bea(0)
        band=True
        j=0 
        while j<len(aux) and band==True:
            if aux[j] == 999:
                band=False
            print(f"aux:{aux[j]}")
            print(f"j{j}")
            j+=1
        return band


    def bea(self, origen):
        cola=Cola(50)
        d = [999] * len(self.matriz)
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
        print(d)
        return d
    

    def bep_visita(self, s, d, f):
        self.tiempo+=1
        d[s] = self.tiempo
        ady=self.adyacente(s)
        for u in ady:
            if d[u] == 0:
                self.bep_visita(u, d, f)

        self.tiempo+=1
        f[s] = self.tiempo


    def bep(self):
        d = [0] * len(self.matriz)
        f = [0] * len(self.matriz)
        for s in range(len(self.matriz)):
            if d[s] == 0:
                self.bep_visita(s, d, f)
        
        return d, f




    
    def distanciaMin(self, distancia, conocido):
        distanciaMin = 999
        indiceMin = -1
        for i in range(len(self.matriz)):
            if distancia[i] < distanciaMin and not conocido[i]:
                distanciaMin = distancia[i]
                indiceMin = i
        return indiceMin
    

    def dijkstra(self, origen):
        conocido = [False] * len(self.matriz)
        distancia = [999] * len(self.matriz)
        distancia[origen] = 0
        camino = [None] * len(self.matriz)

        for _ in range(len(self.matriz)):
            v = self.distanciaMin(distancia, conocido)
            if v == -1:
                break
            conocido[v] = True

            ady=self.adyacente(v)
            for w in ady:
                peso = self.matriz[v][w]
                if not conocido[w]:
                    if distancia[v] + peso < distancia[w]:
                        distancia[w] = distancia[v] + peso
                        camino[w] = v
        return distancia, camino

    def gradSal(self, origen):
        cont=0
        for j in range(len(self.matriz)):
            if self.matriz[origen][j] != 0:
                cont+=1
        return cont
    
    def gradEnt(self, origen):
        cont=0
        for i in range(len(self.matriz)):
            if self.matriz[i][origen] != 0:
                cont+=1
        return cont

    def nodoFuente(self, origen):
        if self.gradSal(origen)>0:
            if self.gradEnt(origen)==0:
                return True
        return False
            


    def mostrar(self):
        for fila in self.matriz:
            print(fila)

if __name__=='__main__':
    grafo=GrafoNoDirigido(6)
    grafo.arista(0,1,3)
    grafo.arista(0,3,6)
    grafo.arista(1,2,1)
    grafo.arista(1,5,1)
    grafo.arista(1,4,2)
    grafo.arista(2,3,2)
    grafo.arista(3,1,3)
    grafo.arista(4,3,3)
    grafo.arista(4,5,2)
    grafo.arista(5,0,5)
    grafo.arista(5,3,1)
    grafo.mostrar()
    print("Adyacente:")
    grafo.adyacente(0)
    print("--------ej3------")
    nombre=(input("Ingrese nombre persona: "))
    if nombre=='ana':
        aux=0
    elif nombre=='belen':
        aux=1
    elif nombre=='cecilia':
        aux=2
    elif nombre=='daniel':
        aux=3
    elif nombre=='ezequiel':
        aux=4
    elif nombre=='federico':
        aux=5
    print(f"aux: {aux}")
    distancia, camino = grafo.dijkstra(aux)
    nombres=[]
    nombres.append('ana')
    nombres.append('belen')
    nombres.append('cecilia')
    nombres.append('daniel')
    nombres.append('ezequiel')
    nombres.append('federico')
    print(nombres)
    for i in range(len(nombres)):
        print(f"Para mandarle sms a {nombres[i]} gasta {distancia[i]} centavos")
        
    
    print(f"Distancia(pesos) desde el nodo 0: {distancia}")
    print(f"Caminos para cada nodo: {camino}")
    
    print("--------GradoEnt------")
    entrada=int(input("Ingrese numero nodo para ver gradoentrada: "))
    print(grafo.gradEnt(entrada))
    salida=int(input("Ingrese numero nodo para ver gradosalida: "))
    print(grafo.gradSal(salida))
    fuente=int(input("Ingrese numero nodo para ver si es fuente: "))
    print(grafo.nodoFuente(fuente))
    sumidero=int(input("Ingrese numero nodo para ver si es sumidero: "))
    resultado=grafo.nodoFuente(sumidero)
    print(not resultado)
    print("--------------")
    grafo.bea(1)
    print("--------------")
    print(grafo.conexo())
    print("Dijkstra: ")
    distancia, camino = grafo.dijkstra(0)
    print(f"Distancia(pesos) desde el nodo 0: {distancia}")
    print(f"Caminos para cada nodo: {camino}")
    d, f = grafo.bep()
    print(f"Arreglo d: {d}")
    print(f"Arreglo f:, {f}")