n = int(input('Сколько билетов хотите купить: '))
age = input('Введите возраст посетителей через пробел: ')
age = list(map(int, age.split()))
sum = 0
for i in age:
    if i < 18:
        sum += 0
    if 18 <= i < 25:
        sum += 990
    if i >= 25:
        sum += 1390
if n > 3:
    sum -= sum * 0.1
print(sum)
