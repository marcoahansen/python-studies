# 3) Crie uma função que receba um valor e informe se ele é positivo ou não.

n = int(input("Informe um número para saber se é positivo ou não: "))
if n > 0:
  print("É posititvo")
elif n == 0:
  print("É zero")
else:
  print("É negativo")
