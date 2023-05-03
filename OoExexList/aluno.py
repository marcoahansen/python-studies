class AlunoAcademia:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imc(self):
        return round(self.peso / (self.altura ** 2), 2)

    def pesoMinimo(self):
        return round(18.5 * (self.altura ** 2), 2)

    def pesoMaximo(self):
        return round(24.9 * (self.altura ** 2), 2)

    def pesoMedio(self):
        return round((self.pesoMinimo() + self.pesoMaximo()) / 2, 2)


aluno = AlunoAcademia(70, 1.75)

print("IMC:", aluno.imc())
print("Peso mínimo:", aluno.pesoMinimo())
print("Peso máximo:", aluno.pesoMaximo())
print("Peso médio:", aluno.pesoMedio())
