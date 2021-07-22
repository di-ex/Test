import re
pas = input('Введите пароль: ')
while not pas or re.search(r'[\s]', pas):
    print("Некорректный пароль!")
    pas = input('Введите пароль: ')
else:
    print("Пароль успешно создан")
END
