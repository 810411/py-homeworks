from urllib.parse import urlencode


def create_token(app_id):
    """
    Создает ссылку для получения ключа доступа token
    :param app_id: <str> ID Вашего приложения ВК
    """
    oauth_data = {
        'client_id': app_id,
        'display': 'page',
        'scope': 'status',
        'response_type': 'token'
    }
    print('?'.join(('https://oauth.vk.com/authorize', urlencode(oauth_data))))


create_token('')  # Заполнить id своего приложения VK
