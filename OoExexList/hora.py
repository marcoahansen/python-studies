class Hora:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ehValida(self):
        return 0 <= self.hora < 24 and 0 <= self.minuto < 60 and 0 <= self.segundo < 60

    def imprime(self):
        print(f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}')

    def diferenca(self, outraHora):
        segundosTotais = (self.hora * 3600 + self.minuto * 60 + self.segundo) - \
            (outraHora.hora * 3600 + outraHora.minuto * 60 + outraHora.segundo)
        novaHora = segundosTotais // 3600
        novoMinuto = (segundosTotais % 3600) // 60
        novoSegundo = (segundosTotais % 3600) % 60
        return Hora(novaHora, novoMinuto, novoSegundo)


hora1 = Hora(14, 20, 30)
hora2 = Hora(12, 10, 15)

print(hora1.ehValida())  # True
print(hora2.ehValida())  # True

hora1.imprime()  # 14:20:30
hora2.imprime()  # 12:10:15

diferenca = hora1.diferenca(hora2)
diferenca.imprime()  # 02:10:15
