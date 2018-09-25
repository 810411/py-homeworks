# from urllib.parse import urlencode
import requests
import time

TOKEN = ''  # Заполнить значением ключа доступа ВК


class UserVK:
    """ Класс для экземпляров описывающих пользователей VK и реализующий поиск общих друзей экземпляров
    Экземпляр класса создается на основе идентификатора пользователя VK"""

    def __init__(self, ids, token=TOKEN):
        """
        :param ids: <str> идентификатор пользователя VK
        :param token: <str> ключ доступа VK
        """
        self.ids = ids
        self.main_info = self.main_info()
        self.id = self.main_info['id']

    def __str__(self):
        return f'https://vk.com/id{self.ids}'

    def __and__(self, other):
        friend_list = set(self.friends) & set(other.friends)
        users_list = []
        for user_id in friend_list:
            time.sleep(0.5)
            users_list.append(UserVK(user_id))
        return users_list

    @property
    def params(self):
        return {
            'access_token': TOKEN,
            'v': '5.85',
        }

    def main_info(self):
        params = self.params
        params['user_ids'] = self.ids
        response = requests.get(f'https://api.vk.com/method/users.get', params).json()
        if 'error' in response:
            print(response['error']['error_msg'])
            exit(1)
        return response['response'][0]

    @property
    def friends(self):
        lst = []
        params = self.params
        params['user_id'] = self.id
        response = requests.get(f'https://api.vk.com/method/friends.get', params).json()
        if 'response' in response:
            lst = response['response']['items']
        return lst

    @property
    def info(self):
        first_name = self.main_info['first_name']
        last_name = self.main_info['last_name']
        return f'{first_name} {last_name}.'


# Создаем двух пользователей, выводим их Имя Фамилию и ссылку на страницу, сравниваем списки друзей, добавляем
# общих друзей в список, выводим Имя Фамилию и ссылку на страницу для общих друзей
user1 = UserVK('5')  # Идентификатор пользователя ВК
print(user1.info, user1)
user2 = UserVK('6')  # Идентификатор пользователя ВК
print(user2.info, user2)
print('Список общих друзей (построение займет какое-то время в зависимости от количества результатов):')
common_friends = user1 & user2
if len(common_friends) == 0:
    print('У данных пользователей общих друзей нет')
else:
    for friend in common_friends:
        print(friend.info, friend)
