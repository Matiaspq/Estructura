from colasecuencial import Cola
import random

if __name__=="__main__":
    frecuencia = 5
    tiempoMaximo = 10
    reloj = 0
    impresora = 0
    tiempoImpresora = 5
    trabajosImpresos = 0
    tiempoEsperaTrabajos = 0
    trabajo = 0
    total = 0

    cola=Cola(50)
    while reloj < tiempoMaximo:
        if random.random()<1/frecuencia:
            print(f"Llego un trabajo en el minuto {reloj}")
            tiempoAsignado = int(input("Cantidad de tiempo que necesita esta impresion: "))
            cola.insertar(tiempoAsignado)

        if impresora == 0:
            if not cola.vacia():
                if trabajo>0:
                    print(f"Trabajo devuelto a la cola con tiempo restante: {trabajo}")
                    cola.insertar(trabajo)
                trabajo = cola.eliminar()
                #tiempoEsperaTrabajos
                #tiempoAcumulado += tiempoEsperaTrabajos
                
                impresora = tiempoImpresora
        reloj += 1
        print(f"Reloj: {reloj}")

        if impresora > 0:
            impresora -= 1
            print(f"Impresora: {impresora}")
            trabajo -= 1
            if trabajo == 0:
                trabajosImpresos += 1
                impresora = 0
            print(f"Trabajo: {trabajo}")
            print(f"Cantidad de trabajos en la cola: {cola.cant}")
            cola.recorrer()

if trabajo>0:
    print(f"Trabajo devuelto a la cola con tiempo restante: {trabajo}")
    cola.insertar(trabajo)
print(f"Cantidad de trabajos sin atender: {cola.cant}")



    
