import threading
from ColaFIFO import ColaFIFO

class ColaFifoSize(ColaFIFO):
    def __init__(self, size):
        self. elementos = []
        self.size = size
        self.condition = threading.Condition()

    def insertar(self, dato):
        self.condition.acquire()
        if len(self.elementos) == self.size:
            self.condition.wait()
        self.elementos.append(dato)
        self.condition.notify()
        self.condition.release()

    def extraer(self):
        self.condition.acquire()
        while len(self.elementos) == 0:
            self.condition.wait()
        elemento = self.elementos.pop(0)
        self.condition.notify()
        self.condition.release()
        return elemento


def main():
    cola = ColaFIFO()

    cola = ColaFIFO()

    # check if esta_vacia()

    print(cola.cola_vacia())

    for i in range (1,6):
        cola.insertar(i)

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()