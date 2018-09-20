import os

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations_dir = os.path.join(current_dir, 'Migrations')

# Создает список имен файлов из заданной директории с фильтрацией по расширению .sql
file_list = os.listdir(migrations_dir) if os.path.isdir(migrations_dir) else []
file_list = list(filter(lambda x: os.path.splitext(x)[1] == '.sql', file_list))


def search_in_sql(file_list_: list, user_string_: str, dir_=migrations_dir):
    """ Принимает список имен файлов и строку введенную пользователем,
    возвращает список имен файлов содержащих строку пользователя """
    for file_ in file_list_.copy():
        file_path = os.path.join(dir_, file_)
        with open(file_path, encoding='UTF-8') as fl:
            text = fl.read()
            if user_string_ not in text:
                file_list_.remove(file_)
    return file_list_


def print_file_list(file_list_: list, dir_=migrations_dir):
    """ Принимает список имен файлов, выводит в консоль имена файлов построчно если их количество < 6 иначе первый и
     последний элементы списка, и длину списка """
    if len(file_list) < 6:
        for file_ in file_list_:
            print(os.path.join(os.path.basename(dir_), file_))
    else:
        print(os.path.join(os.path.basename(dir_), file_list_[0]))
        print('...')
        print(os.path.join(os.path.basename(dir_), file_list_[len(file_list) - 1]))
    print('Всего: {}'.format(len(file_list_)))


if __name__ == '__main__':
    while len(file_list) > 1:
        user_string = input('Введите строку: ')
        file_list = search_in_sql(file_list, user_string)
        print_file_list(file_list)
