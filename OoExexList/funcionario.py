class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def ganhoAnual(self):
        decimo_terceiro = self.salario
        abono_ferias = self.salario / 3
        return (12 * self.salario) + decimo_terceiro + abono_ferias

    def descontoIR(self):
        if self.salario <= 1500:
            return 0
        elif self.salario <= 5000:
            return 0.15 * self.salario
        else:
            return 0.25 * self.salario


funcionario = Funcionario(123, 'João', 3000)

print("Ganho anual:", funcionario.ganhoAnual())
print("Desconto de IR:", funcionario.descontoIR())
