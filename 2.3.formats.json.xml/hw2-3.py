import json
import xml.etree.ElementTree as etree


def parse_by_key(filename, k):
    """ Принимает имя файла и слово для ключа, в зависимости от расширения в имени файла парсит соответствующим образом.
    Возвращает список слов из значений ключей(тегов) по переданному слову для ключа"""
    ext = filename.split('.')[1]
    lst = []
    if ext == 'json':
        with open(filename, encoding='UTF-8') as fl:
            from_json = json.load(fl)
            search_recursive_and_split(from_json, k, lst)
    if ext == 'xml':
        tree = etree.parse(filename.encode('cp1251'))
        from_xml = tree.findall(f'.//{k}')
        for item in from_xml:
            lst += item.text.split()
    if ext == 'txt':
        with open(filename, encoding='UTF-8') as fl:
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


def extract_top_ten(lst):
    """ Выбираем из списка слова длиннее 6 букв, сортируем по длине слов, выводим первые десять неповоторяющихся слов"""
    lst = [word for word in lst if len(word) > 6]
    lst = sorted(lst, reverse=True, key=lambda x: lst.count(x))
    counter = 1
    top_ten = []
    for word in lst:
        if word not in top_ten:
            top_ten.append(word)
            print(f'{counter}. {word}')
            counter += 1
        if counter > 10:
            break
    return top_ten


filenames = ['files/newsafr.txt', 'files/newsafr.json', 'files/newsafr.xml']
for filename in filenames:
    print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для {filename}')
    lst = parse_by_key(filename, 'title') + parse_by_key(filename, 'description')
    extract_top_ten(lst)
