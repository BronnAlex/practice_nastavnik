import re
import os
#from data.mypath import base_path


def clear_name(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    #full_path = os.path.join(base_path + '\\')
    new_name_list = list()
    with open('C:\\Users\\AlexBronn\\PycharmProjects\\practika_nastavnik\\data\\' + file_name, 'r', encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_name_list.append(new_name)
    return new_name_list


def is_cyrilic(name_item: str) -> bool:
    """Проверка на вхождение кирилицы в строку"""

    return bool(re.search('[а-яА-Я]', name_item))


def filter_russ(names_list: list) -> list:
    """Фильрация русских имен0"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrilic(name_item):
            new_names_list.append(name_item)
    return new_names_list

if __name__ == '__main__':
    cleared_name = clear_name('names.txt')

    print(filter_russ(cleared_name))
