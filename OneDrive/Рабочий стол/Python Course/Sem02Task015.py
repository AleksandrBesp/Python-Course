# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# from random import randint

# N=0
# while True:
#     if N<1:
#         N=int(input('Введите количество арбузов: '))
#     else:
#         break

# weight_list = []
# for i in range(0, N):
#     weight_list.append(randint(2, 17))
# print('Список арбузов(кг): {}'.format(weight_list))
# print('Самый легкий арбуз: {} кг'.format(min(weight_list)))
# print('Самый тяжелый арбуз {} кг'.format(max(weight_list)))

# n = 5
# m = [5, 1, 6, 5, 9]

# max_m = m[1]
# min_m = m[2]
# buf = 0
# for i in m:
#     if i >= max_m:
#         max_m = i
#     if i <= min_m:
#         min_m = i
# print(max_m, min_m)
    
# print(f'max {max(m)}, min {min(m)}')


from random import randint
n = int(input('Введите количество арбузов: '))
watermelons = []
for i in range(n):
    watermelons.append(randint(1, 100))
print(watermelons)
print(f"Минимальный арбуз {min(watermelons)}")
print(f"Максимальный арбуз {max(watermelons)}")

# r = randint(1, 100)
# print(f"Рандомное число r - {r}")