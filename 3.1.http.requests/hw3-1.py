import requests
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_names = ['ES.txt', 'DE.txt', 'FR.txt']


def translate_it(file_name, out_lang, dir_=current_dir):
    """
    YANDEX translation plugin
    Read text from file, detect language, translate text in out_lang code language and save it in new file.

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/detect
     ? [key=<API-ключ>]
     & text=<текст>
     & [hint=<список вероятных языков текста>]
     & [callback=<имя callback-функции>]

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param file_name: <str> name of file with text for translate.
    :param out_lang: <str> language code for translation, list of codes:
    https://tech.yandex.ru/translate/doc/dg/concepts/api-overview-docpage/
    :param dir_: <str> directory where placed file with text for translate
    :return: res: <str> result message.
    """

    in_file_path = os.path.join(dir_, file_name)
    file_name_name, file_name_ext = os.path.splitext(file_name)
    file_name = file_name_name + '-' + out_lang.upper() + file_name_ext
    out_file_path = os.path.join(dir_, file_name)

    with open(in_file_path, encoding='utf-8') as fl:
        text = fl.read()

    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    text_fragment = ' '.join(text.split()[:10])
    params = {
        'key': key,
        'text': text_fragment,
    }
    response = requests.get(url, params=params).json()

    lang = '{}-{}'.format(response.get('lang'), out_lang)
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()

    if response.get("code") == 200:
        output = ' '.join(response.get('text', []))
        with open(out_file_path, 'w', encoding='utf-8') as fl:
            fl.write(output)
        res = f'Translated saved to {out_file_path}'
    else:
        res = 'Something went wrong!'

    return res


for file_ in file_names:
    result = translate_it(file_, 'ru')
    print(result)
