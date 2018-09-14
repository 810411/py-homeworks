import json
import xml.etree.ElementTree as etree


def parse_by_key(filename_, k):
    """ Принимает имя файла и слово для ключа, в зависимости от расширения в имени файла парсит соответствующим образом.
    Возвращает список слов из значений ключей(тегов) по переданному слову для ключа"""
    ext = filename_.split('.')[1]
    lst = []
    if ext == 'json':
        with open(filename_, encoding='UTF-8') as fl:
            from_json = json.load(fl)
            search_recursive_and_split(from_json, k, lst)
    if ext == 'xml':
        tree = etree.parse(filename_.encode('cp1251'))
        from_xml = tree.findall(f'.//{k}')
        for item in from_xml:
            lst += item.text.split()
    if ext == 'txt':
        with open(filename_, encoding='UTF-8') as fl:
            for line in fl.readlines():
                lst += line.split()
    return lst


def search_recursive_and_split(obj, k, lst):
    """ Принимает словарь, имя для ключа, список. Рекурсивно ищет по словарям и спискам в исходном словаре
    значения с ключами по имени. К переданному списку добавляет все найденые значения разбытые на отдельные слова """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == k:
                lst += value.split()
            search_recursive_and_split(value, k, lst)
    elif isinstance(obj, list):
        for item in obj:
            search_recursive_and_split(item, k, lst)


def extract_top_ten(list_for_extraction):
    """ Выбираем из списка слова длиннее 6 букв, сортируем по длине слов, выводим первые десять неповоторяющихся слов"""
    list_for_extraction = [word for word in list_for_extraction if len(word) > 6]
    list_for_extraction = sorted(list_for_extraction, reverse=True, key=lambda x: list_for_extraction.count(x))
    counter = 1
    top_ten = []
    for word in list_for_extraction:
        if word not in top_ten:
            top_ten.append(word)
            print(f'{counter}. {word}')
            counter += 1
        if counter > 10:
            break
    return top_ten


file_names = ['newsafr.txt', 'newsafr.json', 'newsafr.xml']
for filename in file_names:
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для {filename}')
    top_ten_list = parse_by_key(f'files/{filename}', 'title') + (
        parse_by_key(f'files/{filename}', 'description') if filename.split('.')[1] != 'txt' else [])
    extract_top_ten(top_ten_list)
