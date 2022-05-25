def read():
    readvar = int(input('Выберите вариант вывода: 1 - для вывода в строку, 2 - для вывода в столбец: '))
    if readvar == 1:
        with open('rowbook.csv', 'r') as file:
            rowres = file.read()
            print(rowres)
    elif readvar == 2:
        with open('columnbook.csv','r') as file:
            columnres = file.read()
            print(columnres)