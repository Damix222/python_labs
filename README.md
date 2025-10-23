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




# Лабораторнгая работа 3

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
    '''
sys.exit(1) интерпретатор сразу завершает работу 
Значение аргумента (1):
Код возврата 1 означает, что программа завершилась с ошибкой.
Код возврата 0 означет успешное завершение программы.
    '''
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