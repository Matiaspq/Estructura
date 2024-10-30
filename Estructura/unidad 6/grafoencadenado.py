class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Valor del nodo
        self.siguiente = None  # Puntero al siguiente nodo en la lista de adyacencia

class Grafo:
    def __init__(self, tamanio):
        self.tamanio = tamanio  # Número de vértices
        self.adj = [None] * tamanio  # Lista de adyacencia

    def agregar_arista(self, origen, destino):
        # Agregar un arco desde 'origen' a 'destino'
        nuevo_nodo = Nodo(destino)  # Crear un nuevo nodo para el destino

        # Insertar el nuevo nodo al principio de la lista de adyacencia del origen
        if self.adj[origen] is None:
            self.adj[origen] = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.adj[origen]  # Apuntar al anterior nodo
            self.adj[origen] = nuevo_nodo  # Actualizar la cabeza

    def mostrar(self):
        for i in range(self.tamanio):
            print(f"Vértice {i}: ", end="")
            nodo_actual = self.adj[i]
            if nodo_actual is None:
                print("None")
            else:
                while nodo_actual is not None:
                    print(nodo_actual.dato, end=" -> ")
                    nodo_actual = nodo_actual.siguiente
                print("None")  # Indica el final de la lista

# Ejemplo de uso
grafo = Grafo(5)  # Grafo con 5 vértices
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(1, 4)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)

grafo.mostrar()  # Mostrar la representación del grafo