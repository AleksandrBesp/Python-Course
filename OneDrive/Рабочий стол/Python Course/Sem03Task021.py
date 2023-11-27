"""
Задача №21. Общее обсуждение
Напишите программу для печати всех уникальных
значений в словаре.

Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально.
Пользователь его не вводит

"""
dictionary = {"I": "S001", "II": "S002", "VI": "S001", "X": "S005", "VII": "S005", "V":"S009", "VIII":"S007"}
my_set = set()
for item in dictionary:
    my_set.add(dictionary[item])

print(my_set)

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# list_2 = []
# dict_1 = {}
# for i in range(len(list_1)):
#     dict_1 = list_1[i]
#     list_2.append(*dict_1.values())
# print(set(list_2))
