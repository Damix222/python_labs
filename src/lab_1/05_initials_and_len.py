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