from src.lab09.group import Group
from src.lab08.models import Student
from pathlib import Path

def print_students(title: str, group: Group):
    print(title)
    for s in group.list():
        print(f"  {s.fio:<20} {s.birthdate} {s.group:<10} {s.gpa}")
    print()

def main():
    csv_path = "data/lab09/students.csv"
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    group = Group(csv_path)
    
    print_students("Исходный CSV:", group)
    
    s1 = Student("Петров Петр", "2007-05-15", "БИВТ-25-6", 4.2)
    group.add(s1)
    print_students("После добавления Петрова:", group)
    
    found = group.find("петр")
    print("Поиск 'петр':")
    for s in found:
        print(f"  {s.fio}")
    
    group.update("Петров Петр", gpa=4.5, group="БИВТ-25-6")
    print_students("После обновления Петрова:", group)
    
    group.remove("Петров Петр")
    print_students("После удаления Петрова:", group)

if __name__ == "__main__":
    main()