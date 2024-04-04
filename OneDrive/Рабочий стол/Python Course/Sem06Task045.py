"""
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод:     Вывод:
300       220 284
"""
# def sum_div(n):
#     summ = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             summ += i
#     return summ


# n = int(input("введите максимальное число: "))


# lst_exclude = []
# for i in range(2, n):
#     m = sum_div(i)
#     if m < n and m != i and (i == sum_div(m)) and i not in lst_exclude:
#         lst_exclude.append(i)
#         lst_exclude.append(m)
#         print(f"{i} {m}")

# #####
# def sum_div(num):
#     s = 0
#     for el in range(1, num // 2 + 1):
#         if num % el == 0:
#             s += el
#     return s

# def func(k):
#     res = []
#     for i in range(1, k+1):
#         if i not in res:
#             m = sum_div(i)
#             if i == sum_div(m) and m != i:
#                 res.append(i)
#                 res.append(m)
#     return res
# print(func(10000))

k = int(input())
lst1 = list()
for i in range(k):
    summa = 0
    for j in  range(1, i//2 +1):
        if i % j == 0:
            summa += j
    lst1.append(tuple([i, summa]))

# print(lst1)

for i in range(len(lst1)):
    for j in range(i, len(lst1)):
        if i != j and lst1[i][0] == lst1[j][1] and lst1[i][1] == lst1[j][0]:
            print(*lst1[i])
