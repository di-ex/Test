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

roll = list(map(int, roll.split()))
roll.append(n)

def merge_sort(roll):
    if len(roll) < 2:
        return roll[:]
    else:
        middle = len(roll) // 2
        left = merge_sort(roll[:middle])
        right = merge_sort(roll[middle:])
        return merge(left, right)
def merge(left, right):
    new_roll = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_roll.append(left[i])
            i += 1
        else:
            new_roll.append(right[j])
            j += 1
    while i < len(left):
        new_roll.append(left[i])
        i += 1
    while j < len(right):
        new_roll.append(right[j])
        j += 1
    return new_roll

def binary_search():
    middle = len(merge_sort(roll)) // 2
    left = 0
    right = len(merge_sort(roll)) - 1

    while merge_sort(roll)[middle] != n and left <= right:
        if n > merge_sort(roll)[middle]:
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
    if len(merge_sort(roll)) == 1:
        print('Число n является единственным в списке')
    elif len(merge_sort(roll)) - 1 == binary_search():
        print('ID элимента, меньше числа n:', binary_search() - 1)
        print('Число n является наибольшим в списке')
    elif binary_search() == 0:
        print('Число n является наименьшим в списке')
        print('ID элимента, больше числа n:', binary_search() + 1)
    else:
        print('ID элимента, меньше числа n:', binary_search() - 1)
        print('ID элимента, больше числа n:', binary_search() + 1)

arr()
