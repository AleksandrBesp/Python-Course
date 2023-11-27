# Задача №19. Общее обсуждение
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

nums = [1, 2, 3, 4, 5]
# print(nums)
k = 3
# # shifted_nums = nums[-k:] + nums[:-k]
# # print(shifted_nums)

new_list = nums[k:] + nums[:k]
print(new_list)

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# shift = 0
# buf = int
# while shift < k:
#     buf = list_1.pop(len(list_1)-1)
#     list_1.insert(0, buf)
#     shift += 1
# print(list_1)