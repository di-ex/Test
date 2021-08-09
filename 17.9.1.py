roll = input('Введите последовательность целых чисел через пробел: ')

def check(roll):
    try:
        roll = list(map(int, roll.split()))
    except ValueError:
        return False
    else:
        return True

while check(roll) is False:
    print("Некорректный ввод!")
    roll = input('Введите последовательность целых чисел через пробел: ')
else:
    n = int(input('Введите любое целое число: '))

def sorty(roll):
    roll = list(map(float, roll.split()))
    roll.append(n)
    roll.sort()
    return roll

def binary_search():
    middle = len(sorty(roll)) // 2
    left = 0
    right = len(sorty(roll)) - 1

    while sorty(roll)[middle] != n and left <= right:
        if n > sorty(roll)[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2

    if left > right:
        return False
    else:
        return middle

print('ID элимента n:', binary_search())

def arr():
    if len(sorty(roll)) == 1:
        print('Число n является единственным в списке')
    elif len(sorty(roll)) - 1 == binary_search():
        print('ID элимента, меньше числа n:', binary_search() - 1)
        print('Число n является наибольшим в списке')
    elif binary_search() == 0:
        print('Число n является наименьшим в списке')
        print('ID элимента, больше числа n:', binary_search() + 1)
    else:
        print('ID элимента, меньше числа n:', binary_search() - 1)
        print('ID элимента, больше числа n:', binary_search() + 1)

arr()
