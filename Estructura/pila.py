class Pila:
    def __init__(self, cant):
        self.cant = cant
        self.tope = -1
        self.items = [0] * cant

    def vacia(self):
        return self.tope == -1

    def insertar(self, x):
        if self.tope < self.cant - 1:
            self.tope += 1
            self.items[self.tope] = x
            return x
        else:
            return 0

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            x = self.items[self.tope]
            self.tope -= 1
            return x

    def mostrar(self):
        if not self.vacia():
            for i in range(self.tope, -1, -1):
                print(self.items[i])


if __name__ == "__main__":

    n = int(input("Número de discos: "))

    pila1 = Pila(n)
    pila2 = Pila(n)
    pila3 = Pila(n)
    pilas = []
    pilas.append(pila1)
    pilas.append(pila2)
    pilas.append(pila3)

    for i in range(n, 0, -1):
        pilas[0].insertar(i)

    for i in range(3):
        print(f"pila {i}: \n")
        pilas[i].mostrar()

    origen=int(input("Pila origen: "))
    destino=int(input("Pila destino: "))

    while origen !=0 or destino != 0:
        print(f"origen: {origen}")
        print(f"destino: {destino}\n")
        disco=pilas[origen-1].suprimir()
        print(f"disco: {disco}")
        disco2=pilas[destino-1].suprimir()
        print(f"disco2: {disco2}")
        if disco!=0:
            if disco2==0:
                pilas[destino-1].insertar(disco)
            elif disco<disco2:
                pilas[destino-1].insertar(disco2)
                pilas[destino-1].insertar(disco)
            else:
                print("\n Disco es mayor que disco2")
                pilas[origen-1].insertar(disco)
                pilas[destino-1].insertar(disco2)


         
        for i in range(3):
            print(f"pila {i}: \n")
            pilas[i].mostrar()
        
        origen=int(input("Pila origen: "))
        destino=int(input("Pila destino: \n"))


