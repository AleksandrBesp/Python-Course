# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# num_list = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(num_list)))

import random
N = int(input("Введите количество чисел: "))

list_1 = []
list_2 = []
for i in range(N):
    list_1.append(random.randint(1, 20))
print(list_1)

for i in list_1:
    if i not in list_2:
       list_2.append(i)
   
print(len(list_2))

# arr = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(arr)))
# #  Традиционный итератор с функцией append()
# lst = []
# for el in arr:
#     if el not in lst:
#         lst.append(el)
# print(len(lst))