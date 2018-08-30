# Задача №1

countries = {
    'Thailand': {'country_sea': True, 'country_schengen': False, 'exchange_rate': 2, 'temperature': 28,
                 'living_cost': 900},
    'Germany': {'country_sea': True, 'country_schengen': True, 'exchange_rate': 74, 'temperature': 10,
                'living_cost': 50},
    'Poland': {'country_sea': True, 'country_schengen': True, 'exchange_rate': 18, 'temperature': 8,
               'living_cost': 150},
    'Russia': {'country_sea': True, 'country_schengen': False, 'exchange_rate': 1, 'temperature': 5,
               'living_cost': 2000}
}
budget = 20000

countries['Zimbabwe'] = {'country_sea': False, 'country_schengen': False, 'exchange_rate': 68, 'temperature': 32,
                         'living_cost': 5}
countries['Turkmenistan'] = {'country_sea': True, 'country_schengen': False, 'exchange_rate': 20, 'temperature': 25,
                             'living_cost': 100}
countries['England'] = {'country_sea': True, 'country_schengen': True, 'exchange_rate': 90, 'temperature': 12,
                        'living_cost': 100}

print('Страны подходящие по условию задания:')
for country, properties in countries.items():
    if (budget / int(properties['exchange_rate']) >= int(properties['living_cost']) * 7 and properties[
        'country_schengen']) \
        or (budget / int(properties['exchange_rate']) >= int(properties['living_cost']) * 10 and properties[
            'country_sea']
            and properties['temperature'] > 20):
        print(country)

# Задача №2

cook_book = {
    'салат':
        [
            ['картофель', 100],
            ['морковь ', 50],
            ['огурцы', 50],
            ['горошек', 30],
            ['майонез', 70],
        ],
    'пицца':
        [
            ['сыр', 50],
            ['томаты', 50],
            ['тесто', 100],
            ['бекон', 30],
            ['колбаса', 30],
        ],
    'фруктовый десерт':
        [
            ['хурма', 60],
            ['киви', 60],
            ['творог', 60],
            ['сахар', 10],
            ['мед', 50],
        ]
}
person = 3

print('Список покупок:')
shopping_list = {(key, value * person) for key, value in sum([i for i in cook_book.values()], [])}
for key, value in shopping_list:
    print('{} - {}'.format(key, value))
