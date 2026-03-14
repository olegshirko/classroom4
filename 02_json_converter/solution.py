# Конвертер CSV в JSON - решение
#
# Задача: Преобразовать users.csv (id,name) в users.json (список словарей)
#
# Алгоритм решения:
# 1. Читаем CSV файл с помощью модуля csv
# 2. Используем DictReader для автоматического создания словарей из заголовков
# 3. Преобразуем результат в список
# 4. Записываем в JSON файл с помощью json.dump()
#
# Формат CSV:
#   id,name
#   1,Alex
#   2,Maria
#
# Формат JSON (результат):
#   [{"id": "1", "name": "Alex"}, {"id": "2", "name": "Maria"}]

import csv
import json

# Открываем CSV файл для чтения
# csv.DictReader автоматически использует первую строку как заголовки
# и создаёт словари для каждой последующей строки
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    # Преобразуем итератор в список словарей
    users = list(reader)

# Записываем результат в JSON файл
# json.dump() сериализует Python-объект в JSON формат
# ensure_ascii=False позволяет сохранять кириллицу без экранирования
with open('users.json', 'w') as f:
    json.dump(users, f)
