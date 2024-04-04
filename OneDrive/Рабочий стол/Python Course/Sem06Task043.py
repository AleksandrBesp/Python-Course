"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: Вывод:
1 2 3 2 3 2
"""
from itertools import count


nums = [1, 2, 3, 2, 3, 3, 3]
my_set = set(nums)
res = []
for el in my_set:
    res.append(nums.count(el) // 2)
print(sum(res))


# arr = [1, 2, 3, 2, 3, 3, 2]
# num = 0
# for i in set(arr):
#         num += arr.count(i) //2
# print(num)


# print(sum([nums.count(el) // 2 for el in set(nums)]))


# lst1 = [1, 2, 3, 2, 3]
# count = 0
# for i in range(len(lst1)):
#     for j in range(i+1, len(lst1)):
#         if i != j and lst1[i] == lst1[j]:
#             count+=1
# print(count)