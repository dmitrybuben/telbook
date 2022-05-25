def write():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel = input('Введите номер телефона: ')
    telnote = input('Введите пометку для номера: ')
    saveview = int(input('Выберите вариант сохранения: 1 - столбец, 2 - строка:'))
    if saveview == 1:
        with open('columnbook.csv','a') as file:
            file.write(f'{name}\n{surname}\n{tel}\n{telnote}\n\n')
    else:
        with open('rowbook.csv','a') as file:
            file.write(f'{name};{surname};{tel};{telnote};\n')
    print('Запись внесена')

    