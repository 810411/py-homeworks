# Домашнее задание к лекции 2.2 «Работа с путями»

## Задача №1
Нужные для работы файлы и заготовка кода находятся на [GitHub](https://github.com/netology-code/Python_course/tree/master/homework/2.3-paths).

Представьте, что вам нужно отыскать файл в формате sql среди десятков других, при этом вы знаете некоторые части этого файла (на память или из другого источника).

1. Программа ожидает строку, которую будет искать (`input()`).
2. После того, как строка введена, программа ищет её во всех файлах, выводит имена найденных файлов построчно и выводит количество найденных файлов.
3. Программа снова ожидает ввод, но теперь поиск происходит только среди отобранных на предыдущем этапе файлов.
4. Программа снова ожидает ввод.
5. ...

Выход из программы программировать не нужно. Достаточно принудительно ее останавливать, для этого можно нажать Ctrl + C. Для получения списка всех файлов используйте стандартные функции из `os` и `os.path`.

Пример на настоящих данных:
```
python3 find_procedure.py
Введите строку: INSERT
... большой список файлов ...
Всего: 301
Введите строку: APPLICATION_SETUP
... большой список файлов ...
Всего: 26
Введите строку: A400M
... большой список файлов ...
Всего: 17
Введите строку: 0.0
Migrations/000_PSE_Application_setup.sql
Migrations/100_1-32_PSE_Application_setup.sql
Всего: 2
Введите строку: 2.0
Migrations/000_PSE_Application_setup.sql
Всего: 1
```
Не забываем организовывать собственный код в функции.

## Задача №2. Дополнительная (не обязательная)
Генерировать абсолютный путь до папки с миграциями. Скрипт при этом лежит в одной папке с папкой 'Migrations', но запускать мы его можем из любой директории - он будет работать корректно.

## Задача №3. Вызов других программ
Нужно написать программу для запуска браузера.

## Задача №4. Дополнительная (не обязательная)
Нужные для домашней работы файлы находятся на [GitHub](https://github.com/netology-code/Python_course/tree/master/homework/2.4-external-programs).

Есть программа ([Image Magick](http://www.imagemagick.org/script/index.php) для Windows и Linux, либо встроенная утилиту sips для mac), которая сжимает фотографии, и есть папка «Source» с самими фотографиями. Каждую фотографию мы хотим уменьшить до 200px в ширину (высота меняется пропорционально). Нужно для каждой фотографии запустить программу и результат работы положить в папку «Result». Обратите внимание, что папки «Result» у пользователя нет и программа будет запущена несколько раз.

Пример (ImageMagic):
```
convert input.jpg -resize 200 output.jpg
```
Пример (sips):
```
sips --resampleWidth 200 input.jpg
```
**Внимание!** sips меняет исходную фотографию. Используйте команду cp для того чтобы переместить фотографию из папки в папку

## Задача №5
Для подготовки к следующей лекции напишите, для чего используются типы данных: `json`, `xml`, `yaml`.

---
Домашнее задание сдается ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/)

Не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.