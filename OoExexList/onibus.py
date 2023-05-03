class Onibus:
    def __init__(self, max_passageiros, preco_passagem):
        self.max_passageiros = max_passageiros
        self.preco_passagem = preco_passagem
        self.qtde_passageiros = 0

    def entrar(self, qtdPassageiros):
        if self.qtde_passageiros + qtdPassageiros <= self.max_passageiros:
            self.qtde_passageiros += qtdPassageiros
            return True
        else:
            return False

    def sair(self, qtdPassageiros):
        if self.qtde_passageiros >= qtdPassageiros:
            self.qtde_passageiros -= qtdPassageiros
            return True
        else:
            return False

    def faturamento(self):
        return self.qtde_passageiros * self.preco_passagem

    def qtdePassageiros(self):
        return self.qtde_passageiros
