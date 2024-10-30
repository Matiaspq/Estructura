class Cola:
    def __init__(self, max):
        self.max = max
        self.pr = 0
        self.ul = 0
        self.cant = 0
        self.items = [0] * max

    def vacia(self):
        return self.cant == 0
    
    def insertar(self, x):
        if self.cant < self.max:
            self.items[self.ul] = x
            self.ul = (self.ul + 1) % self.max
            self.cant += 1
            return x
        else:
            return 0
        
    def eliminar(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            x = self.items[self.pr]
            self.pr = (self.pr + 1) % self.max
            self.cant -= 1
            return x
        
    def recorrer(self):
        if not self.vacia():
            i = self.pr
            j = 0
            while j < self.cant:
                print(self.items[i])
                i = (i + 1) % self.max
                j += 1
    