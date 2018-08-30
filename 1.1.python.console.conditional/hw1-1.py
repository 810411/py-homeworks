# Задача №1

budget = int(input('Введите ваш бюджет на поездку в отпуск, руб.: '))
vacation_duration = int(input('Продолжительность вашего отпуска, дн.: '))
daily_expenses = int(input('Предполагаемые ежедневные расходы, руб.: '))
number_of_countries = int(input('Количество посещаемых стран: '))

costs_of_flying = 50 * 2
exchange_rate = 70

cost_of_vacation_rur = vacation_duration * round(daily_expenses) + costs_of_flying * number_of_countries * exchange_rate
cost_of_vacation_eur = cost_of_vacation_rur // exchange_rate

print('Стоимость вашего путешествия: {} руб. ({} евро)'.format(cost_of_vacation_rur, cost_of_vacation_eur))

if budget < cost_of_vacation_rur:
    deficit_rur = cost_of_vacation_rur - budget
    deficit_eur = deficit_rur // exchange_rate
    print('Вам не хватает {} руб. ({} евро)'.format(deficit_rur, deficit_eur))

# Задача №2


from time import sleep

dolly = ('овца', 'овцы', 'овец')
count = 0
end = int(input('До скольки будем считать перед сном: '))
while True:
    count += 1
    if count == end + 1:
        break
    elif count % 10 == 1 and count != 11:
        n = 0
    elif count % 10 in [2, 3, 4] and count not in [12, 13, 14]:
        n = 1
    else:
        n = 2
    print('{} {}'.format(count, dolly[n]))
    sleep(1)
