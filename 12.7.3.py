money = float(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(map(lambda i: i * money / 100, per_cent.values()))
# deposit = [round(money * i / 100, 2) for i in list(per_cent.values())]
print("Накопленные средства за год:", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
