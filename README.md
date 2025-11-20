# laboratoriti

# Лабораторнгая работа 1

## Задание 1
```python
name = input()
age = int(input())
print(f'Привет, {name}! Через год тебе будет {age+1}')
```
![01_greeting](/images/lab01/01.png)

## Задание 2
```python
a = float(input())
b = float(input())
print(f'sum={round(a+b, 2)};' f' avg={round((a+b)/2, 2)}')
```
![02_sum_avg](/images/lab01/02.png)

## Задание 3
```python
price = int(input())
discount = int(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base}\nНДС: {vat_amount}\nИтого к оплате: {total}')
```
![03_discount_vat](/images/lab01/03.png)


## Задание 4
```python
m = int(input())
print(f'{m//60}:{m%60}')
```
![04_minues_to_hhmm](/images/lab01/04.png)


## Задание 5
```python
name = input()
while '  ' in name:
    name = name.replace('  ', ' ')
ini = name[0]
for i in range(len(name)-1):
    if name[i] == ' ':
        ini += name[i+1]
print(f'ФИО: {name}')
print(f'Инициалы {ini}.')
print(f'Длина (символов): {len(name)-2}')
```
![05_initials_and_len](/images/lab01/05.png)


## Задание 6
```python
N = int(input())
c_True = c_False = 0
for i in range(N):
    name = input().split()
    if name[-1] == 'True':
        c_True += 1
    else: 
        c_False += 1
print(c_True, c_False)
```
![06](/images/lab01/06.png)


## Задание 7
```python
s = input()
s_new = ''
alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
index_1 = 894537858347598347598347598347958
for word in alph:
    if 0 < s.find(word) < index_1:
        index_1 = s.find(word)
index_2 = 583475893475349857
for i in range(len(s)):
    if s[i].isdigit():
        index_2 = min(index_2, i)
step = index_2+1 - index_1
for x in range(index_1, len(s)+1, step):
    s_new += s[x]
print(s_new)
```
![07](/images/lab01/07.png)



# Лабораторнгая работа 2

## Задание 1
```python
print('Вывод на задание min_max:')
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return  'ValueError'
    return (min(nums), max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print('Вывод на задание unique_sorted:')
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print('Вывод на задание flatten:')
def flatten(mat: list[list | tuple]) -> list:
    new_list = []
    for list in mat:
        for element in list:
            if str(element).isdigit():
                new_list.append(element)
            else:
                return 'ValueError'
    return new_list
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![01_arrays](/images/lab02/arrays.png)

## Задание 2
```python
print('Вывод на задание transpose:')
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    row_1len = len(mat[0])
    for row in mat:
        if len(row) != row_1len:
            return 'ValueError'
    return [list(pillar) for pillar in zip(*mat)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
        
print('Вывод на задание row_sums:')
def row_sums(mat: list[list[float | int]]) -> list[float]:
    list_length = (len(row) for row in mat)
    if len(set(list_length)) != 1:
        return 'ValueError'
    result = 0
    return list(map(int, (sum(x) for x in mat)))
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print('Вывод на задание col_sums:')
def col_sums(mat: list[list[float | int]]) -> list[float]:
    list_length = (len(row) for row in mat)
    if len(set(list_length)) != 1:
        return 'ValueError'
    summa_mat = []
    for j in range(len(mat[0])):
        summa = 0
        for i in range(len(mat)):
            summa += mat[i][j]
        summa_mat.append(summa)
    return(summa_mat)
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![02_matrix](/images/lab02/matrix.png)

## Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if not(isinstance(rec, tuple)):
        raise TypeError
    if len(rec) != 3:
        raise ValueError
    fio, group, gpa = rec
    if len(fio) == 0 or len(group) == 0:
        raise ValueError
    if not isinstance(gpa, (int, float)):
        raise TypeError
    if not (0<gpa<=5):
        raise ValueError
    new_rec = ''
    fio = fio.strip().split()
    if len(fio) == 2:
        fio = str(fio[0][0].upper() + fio[0][1:] + fio[1][0].upper() + '., ')
        new_rec += fio
    if len(fio) == 3:
        fio = str(fio[0][0].upper() + fio[0][1:] + ' ' + fio[1][0].upper() + '.' + fio[2][0].upper() + '., ')
        new_rec += fio
    gpa = f'{gpa:.2f}'
    new_rec += 'гр. ' + str(group) + ', ' + 'GPA ' +  str(gpa)
    return new_rec
print(format_record(("Иванов Иван иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01")))

```
![03_tuples](/images/lab02/tuples.png)




# Лабораторнгая работа 3

## Задание 1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text

from re import *
def tokenize(text: str) -> list[str]:
    pattern = r'\b\w+(?:-\w+)*\b'
    return findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for element in tokens:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return dict(sorted(freq.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    items = list(freq.items())
    items.sort(key=lambda x: x[0])           
    items.sort(key=lambda x: x[1], reverse=True)  
    return items[:n]

if __name__ == '__main__':
    print('Вывод на задание normalize:')
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))

    print(("Вывод на задание tokenize:"))
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))

    print('Вывод на задание count_freq + top_n:')
    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
    print(top_n(count_freq(["a","b","a","c","b","a"])))
    print(top_n(count_freq(["bb","aa","bb","aa","cc"])))
```
![01](/images/lab03/01.png)

## Задание 2
```python
import sys
from pathlib import Path

lib_path = Path(__file__).parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.readline()
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
![02](/images/lab03/02.png)




# Лабораторнгая работа 4

## Задание 1
```python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    encoding: кодировка файла ('utf-8' стоит по умолчанию, но можно выбрать 'cp1251' или другую).
    '''
    p = Path(path) 
    return p.read_text(encoding=encoding)


import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
    header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        len_rows = len(rows[0])
        for element in rows:
            if len_rows != len(element):
                raise ValueError("Все строки должны быть одинаковой длины")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
![01](/images/lab04/01.png)

## Задание 2
```python
from src.lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n
import sys

def main(input_path: str = 'data/input.txt', output_path: str = 'data/report.csv', encoding: str = 'utf-8'):
    try:
        text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print('файл не найден')
        sys.exit(1)
    except UnicodeDecodeError:
        print('неправильная кодировка')
        sys.exit(1)

    freq = count_freq(tokenize(normalize(text)))
    sorted_freq= top_n(freq)
    rows = sorted_freq
    header = ("word", "count")
    if rows:
        write_csv(rows, output_path, header=header)
    else:
        write_csv([], output_path, header=header)

    total_words = sum(freq.values())
    unique_words = len(freq)
    top_5 = sorted_freq[:5]

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_5:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
```
### 1 файл
![02](/images/lab04/02_1.png)
![03](/images/lab04/02_2.png)
### Пустой файл:
![04](/images/lab04/02_03.png)
### Кодировка cp1251:
![05](/images/lab04/02_04.png)




# Лабораторнгая работа 5

## Задание 1
```python
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.is_file():
        raise FileNotFoundError('файл не найден')

    with json_path.open(encoding='utf-8') as f:
        data = json.load(f)

    if len(data) == 0:
        raise ValueError('файл пустой')
    
    if not isinstance(data, list):
        raise ValueError('неверный тип файла')
    
    for element in data:
        if not isinstance(element, dict):
            raise ValueError('неверный тип файла')
        
    headers = list(data[0].keys())
    '''
    Порядок колонок как в 1 объекте 
    '''
    with csv_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  
        for row in data:
            row_data = {key: row.get(key, '') for key in headers}
            writer.writerow(row_data)

json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.is_file():
        raise FileNotFoundError('файл не найден')
    
    with csv_path.open(encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            raise ValueError('файл не содержит заголовка')
        data = list(r)
    if not data:
        raise ValueError('файл пуст')
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')
```
#### JSON
![01](/images/lab05/01.png)
#### Результат
![02](/images/lab05/02.png)
#### CSV
![03](/images/lab05/03.png)
#### Результат
![04](/images/lab05/04.png)

## Задание 2
```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if not csv_path.is_file():
        raise FileNotFoundError('файл не найден')
    
    with csv_path.open(encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        rows = list(r)
    
    if not rows:
        raise ValueError("файл пустой")
    
    book = Workbook()
    sheet = book.active
    sheet.title = "Sheet1"

    for row_index, row in enumerate(rows, start=1):
        for col_index, value in enumerate(row, start=1):
            sheet.cell(row=row_index, column=col_index, value=value)

    for column_index in range(1, len(rows[0]) + 1):
        column_letter = get_column_letter(column_index)
        max_length = et_column_letter(col_index)
        max_length = max((len(str(sheet.cell(row=row, column=column_index).value or "")) for row in range(1, len(rows) + 1)), default=8)
        sheet.column_size[col_letter].width = max(max_length, 8)

    book.save(xlsx_path)

csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')  
```

### Результат
![05](/images/lab05/05.png)



# Лабораторнгая работа 6

## Задание 1
```python
import argparse
import sys
from pathlib import Path
from lib.text import normalize, tokenize, count_freq, top_n

def read_file_lines(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError('Файл не найден') 
    if not path.is_file():
        raise ValueError('не является файлом')
    try:
        with path.open(encoding='utf-8') as f:
            return f.readlines()
    except UnicodeDecodeError:
        raise ValueError(f'Невозможно прочитать файл (кодировка не UTF-8)')

def cat_command(input_file, number_lines):
    try:
        lines = read_file_lines(input_file)
        for i, line in enumerate(lines, start=1):
            if number_lines:
                print(f"{i}\t{line.rstrip()}")
            else:
                print(line.rstrip())
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def stats_command(input_file, top_count):
    if top_count <= 0:
        print("top_count должен быть положительным числом", file=sys.stderr)
        sys.exit(1)
    try:
        lines = read_file_lines(input_file)
    except (FileNotFoundError, ValueError) as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    text = ' '.join(lines)
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    most_common = top_n(freq, n=top_count)
    print(f"Top {top_n} words:")
    for word, count in most_common:
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI утилиты для обработки текста")
    subparsers = parser.add_subparsers(dest='command', required=True)

    cat_parser = subparsers.add_parser('cat', help='Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True, help='Входной файл')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    stats_parser = subparsers.add_parser('stats', help='Частоты слов в тексте')
    stats_parser.add_argument('--input', required=True, help='Входной текстовый файл')
    stats_parser.add_argument('--top', type=int, default=5, help='Сколько показать топ слов (по умолчанию 5)')

    args = parser.parse_args()

    if args.command == 'cat':
        cat_command(args.input, args.n)
    elif args.command == 'stats':
        stats_command(args.input, args.top)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main() 
```
#### --Help
![01](/images/lab06/01.png)
#### ТОп слова 
![02](/images/lab06/02.png)


## Задание 2
```python
import argparse
import sys
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def file_exists_or_exit(filepath):
    path = Path(filepath)
    if not path.exists():
        print('файл не найден', file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f'не является файлом', file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных: JSON, CSV, XLSX")
    subparsers = parser.add_subparsers(dest='cmd')

    p1 = subparsers.add_parser('json2csv', help='Конвертировать JSON в CSV')
    p1.add_argument('--in', dest='input', required=True, help='Входной JSON файл')
    p1.add_argument('--out', dest='output', required=True, help='Выходной CSV файл')

    p2 = subparsers.add_parser('csv2json', help='Конвертировать CSV в JSON')
    p2.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p2.add_argument('--out', dest='output', required=True, help='Выходной JSON файл')

    p3 = subparsers.add_parser('csv2xlsx', help='Конвертировать CSV в XLSX')
    p3.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p3.add_argument('--out', dest='output', required=True, help='Выходной XLSX файл')

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv':
            json_to_csv(args.input, args.output)
            print(f'конвертация JSON в CSV выполнена: {args.output}')
        elif args.cmd == 'csv2json':
            csv_to_json(args.input, args.output)
            print(f'конвертация CSV в JSON выполнена:  {args.output}')
        elif args.cmd == 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
            print(f'конвертация CSV в XLSX выполнена: : {args.output}')
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print('ошибка конвертации файла', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### JSON в CSV
![03](/images/lab06/03.png)
#### CSV в XLSX
![04](/images/lab06/04.png)
#### --HELP
![05](/images/lab06/05.png)
