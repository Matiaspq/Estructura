class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None  
        
class HashingEncadenado:
    def __init__(self, tamanio):
        self.arreglo = [None] * tamanio
        self.tamanio = tamanio
        self.arregloCont = [0] * tamanio
        
    def hashingDivision(self, clave):
        return int(clave) % self.tamanio

    def hashingPlegado(self, clave):
        strclave = str(clave)
        xlon = len(strclave)
        if xlon != 1:
            xcant = xlon // 2  # Se divide la longitud de la clave
            xclave = int(strclave[0:xcant]) + int(strclave[xcant:])  # Sumar las mitades
            return self.hashingDivision(xclave)  # Asegurar que la posición esté dentro de la tabla
        else:
            return self.hashingDivision(clave)
        
    def insertar(self, clave):
        indice = self.hashingPlegado(clave)
        nodo = Nodo(clave)
        if self.arreglo[indice] is None:
            self.arreglo[indice] = nodo
            print("Elemento ingresado en la posición:", indice, "con dato:", self.arreglo[indice].dato)
        else:
            nodo.siguiente = self.arreglo[indice]
            self.arreglo[indice] = nodo 
            self.arregloCont[indice] += 1
            print("Elemento ingresado en la posición:", indice, "con dato:", self.arreglo[indice].dato)
        
    def buscar(self, clave):
        indice = self.hashingPlegado(clave)
        nodo_actual = self.arreglo[indice]
        while nodo_actual is not None:
            if nodo_actual.dato == clave:
                print(f"El dato {clave} fue encontrado")
                return True
            nodo_actual = nodo_actual.siguiente
        print(f"El dato {clave} no fue encontrado")
        return False
    
    def mostrar(self): #no pertenece a estructura
        for i in range(self.tamanio):
            print(f"Índice {i}: ", end="")
            nodo_actual = self.arreglo[i]
            if nodo_actual is None:
                print("None")
            else:
                while nodo_actual is not None:
                    print(nodo_actual.dato, end=" -> ")
                    nodo_actual = nodo_actual.siguiente
                print("None")  # Para indicar el final de la lista enlazada

# Ejemplo de uso
hash_table = HashingEncadenado(10)
hash_table.insertar(123)
hash_table.insertar(234)
hash_table.insertar(123)  # Colisión
hash_table.mostrar()
hash_table.buscar(123)
hash_table.buscar(999)     # No encontrado