money = float(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [round(money + (i * money) / 100, 2) for i in list(per_cent.values())]
print("Накопленные средства за год:", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
