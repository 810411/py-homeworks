import csv


with open('output.csv', encoding='utf-8', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)
del flats_list[0]

# TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
# 2) добавьте в код подсчет количества новостроек

newbuilding_count = 0
for flat in flats_list:
    if "новостройка" in flat:
        print("{} {}".format(flat[0], flat[2]))
        newbuilding_count += 1
print('количество новостроек = {}'.format(newbuilding_count))


# TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
# flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1

subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append({"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]})

# 3) Самостоятельно напишите код, который подсчитываети выводит, сколько квартир нашлось у каждого метро.

for key, value in subway_dict.items():
    print('метро {:<25} - {} квартир'.format(key if key != '' else 'отсутствует', len(value)))
