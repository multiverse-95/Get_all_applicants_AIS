import ijson
import pandas as pd
import re

# Функция для парсинга больших json файлов
def parsingBigJson():
    # Путь к файлу json
    file_object = r"D:\recovery\test_ais_t\Json_file\all_applicants.json"
    list_saiv = []  # Список заявителей
    iterat = 1  # Итератор
    fio = ''  # Переменная в которой хранится фио
    last_name = ''  # Переменная для фамилий
    first_name = ''  # Переменная для имен
    patronymic = ''  # Переменная для отчеств
    # Идем по json, парсим данные
    for prefix, type_of_object, value in ijson.parse(open(file_object, encoding="utf-8")):
        # print(prefix, type_of_object, value)
        if prefix == "content.item.lastName":  # Если объект с фамилией
            if value == None:  # Если значение пустое, то пропускаем
                pass
            else:  # Иначе берем значение
                saiv_new = str(value).lower()  # Переводим в нижний регистр
                pattern = re.compile(r'\s+')  # Шаблон для поиска пробелов
                sentence = re.sub(pattern, '', saiv_new)  # Удаляем пробелы
                first_name = sentence  # Переменной first_name присвоим значение sentence
        elif prefix == "content.item.firstName":  # Если объект с именем
            if value == None:  # Если значение пустое, то пропускаем
                pass
            else:  # Иначе берем значение
                saiv_new = str(value).lower()  # Переводим в нижний регистр
                pattern = re.compile(r'\s+')  # Шаблон для поиска пробелов
                sentence = re.sub(pattern, '', saiv_new)  # Удаляем пробелы
                last_name = sentence  # Переменной last_name присвоим значение sentence
        elif prefix == "content.item.patronymic":  # Если объект с отчеством
            if value == None:  # Если значение пустое, то пропускаем
                pass
            else:  # Иначе берем значение
                saiv_new = str(value).lower()  # Переводим в нижний регистр
                pattern = re.compile(r'\s+')  # Шаблон для поиска пробелов
                sentence = re.sub(pattern, '', saiv_new)  # Удаляем пробелы
                patronymic = sentence  # Переменной patronymic присвоим значение sentence
            fio = first_name + ' ' + last_name + ' ' + patronymic  # Записываем в переменную fio, фамилию имя и отчество
            print("Applicant " + str(iterat) + " fio: " + fio)  # Выводим
            list_saiv.append(fio)  # Добавляем в список
            iterat += 1  # Увеличиваем итератор
    iterat = iterat - 1  # В конце уменьшаем итератор на 1
    print("\n")
    # Убираем дубликаты
    saivitels = pd.Series(list_saiv).drop_duplicates().tolist()
    return saivitels


saivitels = parsingBigJson()
# Записываем в файл
with open(r"D:\recovery\test_ais_t\fio\fio_applicants.txt", "w") as file:
    for saivitel in saivitels:
        file.write(saivitel + '\n')
# Закрываем файл
file.close()
# Выводим сообщение об успешном результате
print("File success write!")
