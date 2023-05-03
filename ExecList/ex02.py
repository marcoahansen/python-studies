import math


print("Escolha uma das figuras para calcular a área:")
print("1 - Círculo")
print("2 - Retângulo")
print("3 - Triângulo")

option = int(input("Digite a opção escolhida (1, 2, ou 3): "))

if option == 1:
    radius = float(input("Digite o raio do círculo: "))
    area = round(math.pi * radius ** 2)
    print(f"A aréa do círculo é: {area}")
elif option == 2:
    base = float(input("Digite a base do retângulo: "))
    height = float(input("Digite a altura do retângulo: "))
    area = round((base * height))
    print(f"a aréa do retângulo é: {area}")
elif option == 3:
    base = float(input("Digite a base do triângulo: "))
    height = float(input("Digite a altura do triângulo: "))
    area = round((base * height) / 2)
    print(f"a aréa do triângulo é: {area}")
else:
    print("Você precisa escolher uma das figuras das opções: 1, 2 ou 3")
    
