import requests


# Функция для получения большого json файла с сервера
def download_file(url):
    # Путь к файлу, куда он будет сохранен
    local_filename = r"D:\recovery\test_ais_t\Json_file\all_applicants.json"
    # payload для запроса
    payload = {"searchString": "", "page": 0, "start": 0, "limit": 100000, "pageSize": 100000}
    # Отправка post запроса
    r = requests.post(url, headers={'Cookie': 'JSESSIONID=cookie_value'}, # Добавление cookies в header
                      json=payload, stream=True)  # добавление payload ка запросу
    # Запись в файл json
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # Запись
                f.write(chunk)
    return local_filename


print('Start post request...')
# Адрес запроса
url = "http://192.168.99.91/cpgu/action/grid/requesters?_dc=1620352057843"
# Вызов функции загрузки ответа в виде json
download_file(url)
# Вывод об успешном результате
print('Success write big json file!')
