📘 Работа с файлами в Python: Полный разбор задач

Этот гайд содержит подробные объяснения и эталонные решения для лабораторных работ первого курса. Используйте его для понимания логики работы с данными.

01. Фильтрация чисел

Задача: Извлечь четные числа из текстового файла и сохранить их через запятую.

Логика решения:

Данные из файла всегда читаются как строки (str).

Чтобы проверить четность, нужно очистить строку от лишних символов (.strip()) и привести к типу int().

После фильтрации числа нужно снова превратить в строки, чтобы метод ",".join() смог собрать их в одну строку для записи.

```Python 
with open('input.txt', 'r', encoding='utf-8') as f:
    # Читаем все строки, убирая пустые
    nums = [line.strip() for line in f if line.strip()]
    
    # Фильтруем только четные (с преобразованием типов)
    result = [n for n in nums if int(n) % 2 == 0]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(result))
```

02. Конвертер CSV в JSON

Задача: Преобразовать таблицу (CSV) в структурированный формат (JSON).

Логика решения:

Первая строка файла содержит названия ключей (заголовки).

Все остальные строки - это значения.

Функция zip() - идеальный инструмент, чтобы "склеить" список заголовков и список значений в один словарь.

```Python 
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    lines = [l.strip().split(',') for l in f if l.strip()]

headers = lines[0] # ['id', 'name']
# Создаем список словарей через генератор
data = [dict(zip(headers, row)) for row in lines[1:]]

with open('users.json', 'w', encoding='utf-8') as f:
    # indent=4 делает JSON читаемым, ensure_ascii=False сохраняет кириллицу
    json.dump(data, f, indent=4, ensure_ascii=False)
```

03. Обработка ошибок (Try/Except)

Задача: Безопасное чтение файла, который может отсутствовать.

Логика решения:

Использование try...except гарантирует, что программа не завершится аварийно при отсутствии файла data.txt.
```Python 
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    content = 'ERROR'

with open('log.txt', 'w', encoding='utf-8') as f:
    f.write(content)
```

04. Анализ логов

Задача: Подсчитать количество строк с определенным статусом (например, "404").

Логика решения:

Чтение файла целиком через .read() может переполнить память, если лог огромный. Правильнее перебирать файл построчно в цикле for.
```Python 
count = 0
with open('server.log', 'r', encoding='utf-8') as f:
    for line in f:
        if '404' in line:
            count += 1

with open('stats.txt', 'w', encoding='utf-8') as f:
    f.write(str(count))
```

05. Патч конфигурации

Задача: Изменить значение конкретного параметра в файле, не меняя остальное.

Логика решения:

Файлы нельзя редактировать "в середине". Нужно прочитать весь файл в список строк, заменить нужный элемент и перезаписать файл полностью.
```Python 
with open('config.env', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('DEBUG=False'):
        # Не забываем добавлять \n в конце строки!
        lines[i] = 'DEBUG=True\n'

with open('config.env', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```

06. Бинарные данные (Magic Bytes)

Задача: Распознать формат файла по его сигнатуре.

Логика решения:

Используется режим 'rb' (read binary). Мы сравниваем первые байты файла с известной константой формата (например, PNG начинается с байтов \x89PNG).
```Python 
with open('file.bin', 'rb') as f:
    header = f.read(4)

# Сравнение с байтовой строкой
res = 'PNG' if header == b'\x89PNG' else 'UNKNOWN'

with open('type.txt', 'w', encoding='utf-8') as f:
    f.write(res)
```

07. Рекурсивный поиск файлов

Задача: Найти все текстовые файлы во всех вложенных директориях.

Логика решения:

Модуль os.walk() - мощный инструмент, который проходит по всем папкам и подпапкам, возвращая списки имен файлов на каждом уровне.
```Python 
import os

found = []
for root, dirs, files in os.walk('project'):
    for file in files:
        if file.endswith('.txt'):
            found.append(file)

with open('found.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(found))
```

⚠️ Типичные ошибки:

Забытая кодировка: Всегда указывайте encoding='utf-8', иначе на Windows русские буквы превратятся в "кракозябры".

Типы данных: Помните, что read() возвращает строку. Для математики используйте int() или float().

Метод записи: f.write() принимает только одну строку. Если нужно записать список строк, используйте f.writelines() или "\n".join(list).

Режим 'w': Помните, что открытие в режиме 'w' моментально стирает всё содержимое файла. Для добавления данных используйте 'a' (append).