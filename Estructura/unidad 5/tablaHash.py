import random

class TablaHash():
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
    
    def hashDivision(self, clave):
        return clave % self.tamaño
    
    def insertar(self, clave):
        print(f"Clave: {clave}")
        i = self.hashDivision(clave)
        print(f"Indice: {i}")
        while self.tabla[i] is not None:
            print(f"el indice {i} esta ocupado buscando en la otra posicion...")
            i = (i + 1) % self.tamaño
        self.tabla[i] = clave

    def buscar(self, clave):
        i = self.hashDivision(clave)
        contador=0
        while self.tabla[i] is not None:
            if self.tabla[i] == clave:
                return contador
            contador+=1
            i = (i + 1) % self.tamaño
        return contador
    
    def mostrar(self):
        for i in self.tabla:
            print(i)
        

if __name__=='__main__':
    tablaprimo=19  #1009  
    tablanoprimo=10  #1000
    numeros=[]
    for i in range(10):
        aleatorio=random.randint(0,1000)
        numeros.append(aleatorio)
    print(numeros)
    tabla=TablaHash(tablaprimo)
    print("---Tabla primo---")
    for i in numeros:
        tabla.insertar(i)
    tabla.mostrar()
    numero=random.randint(0,1000)
    print(f"numero: {numero}")
    i=tabla.buscar(numero)
    print(f"Busca: {numero} {i}")

    print("---Tabla no primo---")
    tablan=TablaHash(tablanoprimo)
    for i in numeros:
        tablan.insertar(i)
    tablan.mostrar()

    
