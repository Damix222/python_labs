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
    if not isinstance(gpa, (int, float)) or not (0<gpa<=5):
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

