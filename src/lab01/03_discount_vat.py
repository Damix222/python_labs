price = int(input())
discount = int(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base}\nНДС: {vat_amount}\nИтого к оплате: {total}')