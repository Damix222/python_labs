import json
from pathlib import Path
from .models import Student

def students_to_json(students: list[Student], path: str):
    path = Path(path)
    data = [s.to_dict() for s in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    


def students_from_json(path: str) -> list[Student]:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив студентов")

    students = []
    for item in data:
        students.append(Student.from_dict(item))

    return students