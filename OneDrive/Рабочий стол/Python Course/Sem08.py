"""
Задача №49. Общее обсуждение
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    first_name = "Иван"
    last_name = "Иванов"
    phone_number = "898575484545"
    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

# ///////////////////////////////////////////////////////////////////////////////////////////////


# def guide():
#     question_1 = input('[1] -- Внесение данных'
#                        '\n[2] -- Вывод всех данных справочника'
#                        '\n[3] -- Поиск по одной из характеристик (фамилия, имя, отчество, номер телефона)\n')

#     if question_1 == '1':
#         with open('guide.txt', 'a', encoding='utf-8') as f:
#             surname = input('Введите фамилию: ')
#             name = input('Введите имя: ')
#             mid_name = input('Введите отчество: ')
#             tel_number = input('Введите номер телефона: ')
#             f.write(f'==========\n{surname} {name} {mid_name} - {tel_number}\n')
#         print('[*] Данные внесены.')

#     elif question_1 == '2':
#         with open('guide.txt', 'r', encoding='utf-8') as f:
#             print(f.read())

#     elif question_1 == '3':
#         with open('guide.txt', 'r', encoding='utf-8') as f:
#             get_info = input('Введите данные для поиска: ')
#             for el in f:
#                 words = el.strip().split()
#                 for word in words:
#                     if word.lower() == get_info.lower():
#                         print(f'\n[*] -- {el}')


# if __name__ == '__main__':
#     guide()


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def insert_person(filename, person):
#     with open(filename, 'a', encoding='utf-8') as f_obj:
#         f_obj.write(f"{person}\n")


# def print_file(filename):
#     with open(filename, 'r', encoding='utf-8') as f_obj:
#         content = f_obj.read()
#         print(content)


# def seek_in_file(filename, keyword):
#     with open(filename, 'r', encoding='utf-8') as f_obj:
#         for line in f_obj:
#             lst = line.split()
#             if keyword in lst:
#                 print(line)


# command = input("Введите команду: Новая запись - new, вывод списка - list, найти - seek, выход - exit: ")
# while command != 'exit':
#     if command == 'new':
#         insert_person('guid.txt', input("Введите Фамилию Имя Отчество и телефон через пробел: "))
#     if command == 'list':
#         print_file('guid.txt')
#     if command == 'seek':
#         seek_in_file('guid.txt',input("Введите ключевое слово: "))
#     command = input("Введите команду: Новая запись в справочке - new, выход - exit: ")

# /////////////////////////////////////////////////////////////////////////////////////////////////////////


"""
Д.З.
Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

Формат сдачи: ссылка на пулл в свой репозиторий
"""