
def itog(summa, procent, date):
    resalt = summa * (1 + (procent * 100) / 100) ** date
    print("Итоговая сумма: ", resalt)

summa = int(input("Введите начальную сумму: "))
procent = float(input("Введите процентную ставку(в виде десятичной дроби): "))
date = int(input("Введите количество лет: "))

itog(summa, procent, date)
