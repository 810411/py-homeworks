import os
import subprocess

# создает абсолютные пути для целевых директорий
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, 'Source')
result_dir = os.path.join(current_dir, 'Result')
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

# Создает список имен файлов из заданной директории с фильтрацией по расширению .jpg
file_list = os.listdir(source_dir) if os.path.isdir(source_dir) else []
file_list = list(filter(lambda x: os.path.splitext(x)[1] == '.jpg', file_list))


def convert_with_convert(file_, argument_, argum_value, dir_: tuple):
    """ Принимает имя файла jpg, аргумент и значение запуска программы convert.exe, названия целевых директорий
    Выполняет вызов процесса для convert.exe дожидается выполнения и выводит результирующее сообщение"""
    input_path = os.path.join(dir_[1], file_)
    output_path = os.path.join(dir_[2], file_)
    converter = os.path.join(dir_[0], 'convert.exe')
    code = subprocess.call(args=[converter, input_path, argument_, argum_value, output_path])
    if code == 0:
        print(f"Well done! Converted to {output_path}")
    else:
        print("Something went wrong!")


if __name__ == "__main__":
    dirs = (current_dir, source_dir, result_dir)
    # В цикле перебираем имена файлов из списка и передаем их в функцию вместе с аргументом запуска и списком директорий
    for file_jpg in file_list:
        convert_with_convert(file_jpg, '-resize', '200', dirs)
