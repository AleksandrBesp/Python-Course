"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:               Вывод:
7                   3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""

# from random import randint

# n = int(input('Введите число (кол-во эл. 1-го массива): '))
# m = int(input('Введите число (кол-во эл. 2-го массива): '))
# first_lst = [randint(1, 15) for i in range(0, n)]
# second_lst =[randint(1, 15) for j in range(0, m)]
# result = []

# for num in first_lst:
#     if num not in second_lst:
#         result.append(num)

# print(f'{first_lst}\n{second_lst}\n{result}')

# lst_3 = list(map(int, input('Введите числа через пробел: ').split()))




# lst_1 = [3, 1, 3, 4, 2, 4, 12]
# lst_2 = [4, 15, 43, 1, 15, 1]
# lst_new = list()
# # традиционный итератор с функцией append
# for el in lst_1:
#     if el not in lst_2:
#         lst_new.append(el)
# print(lst_new)

# # списковые включения LC
# lst_new = [el for el in lst_1 if el not in lst_2]
# print(lst_new)

# ////////////////////////////////////////

from itertools import count


n = int(input('Введите количество элементов первого массива: '))
list1 = list()
for i in range (n):
    x=int(input('Введите число: '))
    list1.append(x)

m = int(input('Введите количество элементов второго массива: '))
list2 = list()
for i in range (m):
    x=int(input('Введите число: '))
    list2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count+=1
    if count == 0:
        print(list1[i])
    count = 0
