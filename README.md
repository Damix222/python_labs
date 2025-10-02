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




