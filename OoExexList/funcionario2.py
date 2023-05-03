class Funcionario:
    def __init__(self, matricula, nome, salario, ativo=True):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        self.ativo = ativo

    def aumenta(self, percentual):
        self.salario *= (1 + percentual/100)

    def demite(self):
        self.ativo = False


# Criando um funcionário
funcionario1 = Funcionario(1, "João", 2000.00)

# Aumentando o salário do funcionário em 10%
funcionario1.aumenta(10)

# Demitindo o funcionário
funcionario1.demite()

# Verificando se o funcionário está ativo
print(funcionario1.ativo)  # False
