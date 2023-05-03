class Numero:
    def __init__(self, n):
        self.n = float(n)

    def fatorial(self):
        if self.n < 0:
            return None
        else:
            fat = 1
            for i in range(1, int(self.n) + 1):
                fat *= i
            return fat

    def potencia(self, x):
        return self.n ** x

    def parteInteira(self):
        return int(self.n)

    def parteDecimal(self):
        return self.n - int(self.n)


numero = Numero(5)

print("Fatorial:", numero.fatorial())
print("Potência de 2:", numero.potencia(2))
print("Parte inteira:", numero.parteInteira())
print("Parte decimal:", numero.parteDecimal())
