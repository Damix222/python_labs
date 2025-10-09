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
