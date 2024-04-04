"""Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод:                                      Вывод:
values = [0, 2, 10, 6]                      same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
"""
from unittest import result

def same_by(characteristic, object):
    result = True
    list1 = [characteristic(x) for x in object]
    for i in range(len(list1)-1):
        if list1[i] != list1[i+1]:
            result = False
    return result


values = [1, 3, 7, 1]                     
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')