class Cuenta():
    def __init__(self, num, sal=0):
        self.numero = num
        self.saldo = sal

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        self.saldo = self.saldo - cantidad
