"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""
lst = "a a a b c a a d c d d".split()
print(lst)
dct = {}
for item in lst:
    if item in dct:
        print(f"{item}_{dct[item]}", end = ' ')
    else:
        print(item, end = ' ')
    dct[item] = dct.get(item, 0) + 1

# some_str = 'a a a b c a a d c d d'.split()
# a = ''

# for i in some_str:
#     count = a.count(i)
#     if a.count(i) == 0:
#         a += i + ' '
#     else:
#         a += i + '_' + str(count) + ' '

# print(a)