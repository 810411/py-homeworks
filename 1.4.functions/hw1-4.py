documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_person_by_doc_number():
    """
    Запрашивает на ввод номер документа и выводит имя человека,
    если номер найден в словаре из списка 'documents', иначе 'Соответствий не найдено'
    """
    doc_number = input('Введите номер документа: ')
    people = 'Соответствий не найдено'
    for document in documents:
        if document['number'] == doc_number:
            people = document['name']
    print(people)


def print_list_of_documents():
    """ Выводит список всех документов """
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))


def search_shelf_by_doc_number(doc_number=''):
    """
    Запрашивает на ввод номер документа и печатает номер полки где находится документ,
    если документ найден в словаре 'directories', иначе 'Соответствий не найдено',
    опционально принимает номер документа и возвращает номер полки
    """
    printable = False
    if doc_number == '':
        doc_number = input('Введите номер документа: ')
        printable = True
    shelf = 'Соответствий не найдено'
    for key, value in directories.items():
        if doc_number in value:
            shelf = key
    if printable:
        print(shelf)
    return shelf


def adding_doc(shelf='', doc_number=''):
    """ Добавляет новую запись в 'documents', 'directories' """
    if shelf == '':
        new_doc = input('Введите, через запятую, номер документа, тип, имя владельца и номер полки:')
        new_doc = format_input(new_doc)
        documents.append({"type": new_doc[1], "number": new_doc[0], "name": new_doc[2].title()})
        shelf = new_doc[3]
        doc_number = new_doc[0]
        print('Документ "{}" добавлен'.format(doc_number))
    if shelf not in directories.keys():
        adding_shelf(shelf)
    directories[shelf].append(doc_number)


def deleting_doc(remove_in_docs=True, doc_number=''):
    """ Удаляет запись из 'documents', 'directories' по введенному номеру"""
    if doc_number == '':
        doc_number = input('Введите номер документа: ')
    try:
        if remove_in_docs:
            [(documents.remove(_), print('Документ "{}" удален'.format(doc_number))) for _ in documents if
             doc_number in _.values()]
        [value.remove(doc_number) for value in directories.values() if doc_number in value]
    except ValueError:
        print('Соответствий не найдено')


def adding_shelf(shelf_number=''):
    """ Добавляет новую полку в 'directories' """
    if shelf_number == '':
        try:
            shelf_number = int(input('Введите номер новой полки: '))
        except TypeError:
            print('Полка не добавлена. Номер полки должен быть целым числом')
            return
    shelf_number = str(shelf_number)
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        print('Добавлена полка: {}'.format(shelf_number))
    else:
        print('Такая полка уже существует')


def moving_doc_inter_shelves():
    """ Перекладывает документ на указанную полку в 'directories' """
    coordinates = input('Введите, через запятую, номер документа и полки куда его переложить: ')
    coordinates = format_input(coordinates)
    doc_number, target_shelf = coordinates[0], coordinates[1]
    current_shelf = search_shelf_by_doc_number(doc_number)
    if current_shelf != 'Соответствий не найдено':
        deleting_doc(False, doc_number)
        adding_doc(target_shelf, doc_number)
        print('Документ {} перемещен с полки {} на полку {}'.format(doc_number, current_shelf, target_shelf))


def format_input(user_input):
    """ Форматирует пользовательский ввод с несколькими значениями в список """
    user_input = user_input.split(',')
    user_input = [_.strip() for _ in user_input]
    return user_input


functions = {
    'p': search_person_by_doc_number,
    'l': print_list_of_documents,
    's': search_shelf_by_doc_number,
    'a': adding_doc,
    'd': deleting_doc,
    'm': moving_doc_inter_shelves,
    'as': adding_shelf
}

while True:
    command = input('Введите команду ("q" - выход): ')
    if command == 'q':
        break
    if command in functions.keys():
        functions[command]()
    else:
        print('Команда не найдена, повторите ввод')
