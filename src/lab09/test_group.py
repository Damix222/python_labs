import tempfile
from pathlib import Path
from src.lab09.group import Group
from src.lab08.models import Student


# Создаём тестовый CSV
def create_temp_csv():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w", encoding="utf-8")
    tmp.write(
        "fio,birthdate,group,gpa\n"
        "Сидоров Пётр Алексеевич,2007-02-15,БИВТ-25-5,4.1\n"
        "Кузнецова Анна Сергеевна,2007-07-29,БИВТ-25-5,4.8\n"
        "Морозов Дмитрий Павлович,2006-11-03,БИВТ-25-6,3.9\n"
        "Алексеева Мария Викторовна,2007-05-21,БИВТ-25-6,4.5\n"
        "Волков Сергей Петрович,2007-03-12,БИВТ-25-6,3.7\n"
    )
    tmp.close()
    return Path(tmp.name)


def test_list():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    students = g.list()

    assert len(students) == 5
    assert students[0].fio == "Сидоров Пётр Алексеевич"


def test_find():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    res = g.find("Анна")
    assert len(res) == 1
    assert res[0].fio == "Кузнецова Анна Сергеевна"


def test_add():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    new_student = Student("Новый Студент", "2007-01-01", "БИВТ-00-0", "5.0")
    g.add(new_student)

    students = g.list()
    assert len(students) == 6
    assert students[-1].fio == "Новый Студент"


def test_remove():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    removed = g.remove("Морозов Дмитрий Павлович")

    assert removed == 1
    students = g.list()
    assert len(students) == 4
    assert all(s.fio != "Морозов Дмитрий Павлович" for s in students)


def test_update():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    updated = g.update("Волков Сергей Петрович", gpa="4.9")

    assert updated is True

    students = g.list()
    volkov = next(s for s in students if s.fio == "Волков Сергей Петрович")
    assert volkov.gpa == "4.9"


def test_update_missing():
    csv_path = create_temp_csv()
    g = Group(csv_path)

    updated = g.update("Несуществующий", gpa="5.0")

    assert updated is False