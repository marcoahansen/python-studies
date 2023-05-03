# diga se um ano é bissexto ou não

year = int(input("Digite um ano para saber se ele é bissexto: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "é um ano bissexto!")
else:
    print(year, "não é um ano bissexto!")

# quantos anos bissextos aconteceram entre o ano 1 e o ano 2010

startYear = 1
endYear = 2010

leapYears = (endYear // 4 - endYear // 100 + endYear // 400) - ((startYear-1) // 4 - (startYear-1) // 100 + (startYear-1) // 400)

print(f"Entre o ano {startYear} e o ano {endYear} aconteceram {leapYears} anos bissextos")