n = int(input('Сколько билетов хотите купить: '))
age = input('Введите возраст посетителей через пробел: ')
age = list(map(int, age.split()))
summa = 0
for i in age:
    if i < 18:
        summa += 0
    if 18 <= i < 25:
        summa += 990
    if i >= 25:
        summa += 1390
if n > 3:
    summa -= summa * 0.1
print('Сумма к оплате:', sum)
