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
