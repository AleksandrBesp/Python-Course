'''
Задача №36
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Пример

На входе:


print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:


1 2 3
2 4 6 
3 6 9
'''
# Введите ваше решение ниже
def print_operation_table(operation, num_rows, num_columns):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))





#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

print_operation_table(lambda x, y: x * y, 3, 3)
# print_operation_table(lambda x, y: x + y, 4, 4)

"""
Не все тесты пройдены, есть ошибки :(


Количество затраченных попыток: 3

Время выполнения: 1.264847 сек

Общая статистика
Всего тестов: 6. Пройдено: 2. Не пройдено: 4.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x * y, 3, 3)
Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x + y, 4, 4)


Ожидаемый ответ:

2 3 4 5
3 4 5 6
4 5 6 7
5 6 7 8

Ваш ответ:

1 2 3 4
2 4 5 6
3 5 6 7
4 6 7 8
Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x - y, 5, 5)


Ожидаемый ответ:

0 -1 -2 -3 -4
1 0 -1 -2 -3
2 1 0 -1 -2
3 2 1 0 -1
4 3 2 1 0

Ваш ответ:

1 2 3 4 5
2 0 -1 -2 -3
3 1 0 -1 -2
4 2 1 0 -1
5 3 2 1 0
Тест 4
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x * y, 1, 2)
Тест 5
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x / y, 4, 4)


Ожидаемый ответ:

1.0 0.5 0.3333333333333333 0.25
2.0 1.0 0.6666666666666666 0.5
3.0 1.5 1.0 0.75
4.0 2.0 1.3333333333333333 1.0

Ваш ответ:

1 2 3 4
2 1.0 0.6666666666666666 0.5
3 1.5 1.0 0.75
4 2.0 1.3333333333333333 1.0
Тест 6
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

def print_operation_table(operation, num_rows, num_columns):
    if num_rows <= 2 or num_columns <= 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# print_operation_table(lambda x, y: x * y, 4, 4) 

print_operation_table(lambda x, y: x * y)


Ожидаемый ответ:

1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81

Ошибка:

Traceback (most recent call last):
  File "V5G5HBIRMCHY7QYQC219.py", line 27, in <module>
    print_operation_table(lambda x, y: x * y)
TypeError: print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'
"""