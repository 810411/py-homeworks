def ingredient_line_to_dict(ingredient):
    """ Разбиваем принятую строку описания ингридиента в словарь по заданным ключам """
    ingredient_dict = {}
    ingredient = ingredient.split('|')
    ingredient_dict['ingredient_name'] = ingredient[0].strip()
    ingredient_dict['quantity'] = int(ingredient[1])
    ingredient_dict['measure'] = ingredient[2].strip()
    return ingredient_dict


def read_cook_book():
    """ Читаем файл рецептов в словарь по заданному шаблону """
    cook_book = {}
    with open('recipies.txt', 'r', encoding='UTF-8') as fl:
        for line in fl:
            line = line.strip()
            cook_book[line] = []
            for _ in range(int(fl.readline())):
                cook_book[line].append(ingredient_line_to_dict(fl.readline()))
            fl.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """ Принимает список названий блюд (из файла рецептов) и количество персон,
    возвращает словарь с необходимыми ингридентами """
    ingredients_dict = {}
    cook_book = read_cook_book()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            key = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            if key in ingredients_dict:
                ingredients_dict[key]['quantity'] += quantity
            else:
                ingredients_dict[key] = {
                    'measure': ingredient['measure'],
                    'quantity': quantity
                }
    return ingredients_dict


list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for key, value in list_by_dishes.items():
    print(f"'{key}': {value}")
