
print("Descubra se um valor é divisível pelo outro:")
a = int(input("Digite o valor que será dividido: "))
b = int(input("Digite o valor para dividir: "))

divisible = a % b 

if divisible == 0:
    print(f"O número {a} é divisível pelo número {b} =)")
else:
    print(f"O número {a} não é divisível pelo número {b} =(")