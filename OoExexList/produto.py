class Produto:
    def __init__(self, codigo, descricao, preco_custo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.preco_venda = None
        self.margem_lucro = None

    def setMargemLucro(self, percentual):
        self.margem_lucro = percentual
        self.preco_venda = self.preco_custo * (1 + self.margem_lucro/100)

    def setPrecoVenda(self, valor):
        self.preco_venda = valor
        self.margem_lucro = ((self.preco_venda/self.preco_custo) - 1) * 100


p1 = Produto(1, 'Camiseta', 10.0)
print(f'Preço de custo: {p1.preco_custo:.2f}')
p1.setMargemLucro(50)
print(f'Preço de venda: {p1.preco_venda:.2f}')
print(f'Margem de lucro: {p1.margem_lucro:.2f}%')
p1.setPrecoVenda(20)
print(f'Preço de venda: {p1.preco_venda:.2f}')
print(f'Margem de lucro: {p1.margem_lucro:.2f}%')
