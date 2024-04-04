"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:         Ввод:
5 5
1 2 3 4 5     1 5 1 5 1
Вывод:        Вывод:
0             2
(каждое число вводится с новой строки)
"""
# lst = [1, 5, 1, 5, 1]
# count = 0
# for i in range(1, len(lst) - 1):
#     if lst[i - 1] < lst[i] > lst[i + 1]:
#         count += 1

# print(count)

# def search_el(list_el):
#     count = 0
#     for i in range(1, len(list_el) - 1):
#         if list_el[i] > list_el[i-1] and list_el[i] > list_el[i+1]:
#             count += 1
#     return count


# list1 = [1, 6, 3, 6, 5, 7, 4]
# print(search_el(list1))


# my_set = set()
# for el in range(10):
#     my_set.add(el)


# my_set = {el for el in range(10)}

# my_dict = {}
# for el in range(10):
#     my_dict[el] = str(el)

# my_dict = {el: str(el) for el in range(10)}

n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

count = 0
for i in range (1, n-1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count+=1

print(count)