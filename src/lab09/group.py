import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student

class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.HEADER)
                writer.writeheader()

    def _read_all(self) -> List[dict]:
        if not self.path.exists() or self.path.stat().st_size == 0:
            return []
        try:
            with self.path.open("r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames != self.HEADER:
                    raise ValueError("Неверный заголовок CSV")
                return list(reader)
        except csv.Error:
            return []

    def _write_all(self, rows: List[dict]) -> None:
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        rows = self._read_all()
        return [Student.from_dict(r) for r in rows]


    def add(self, student: Student) -> bool:
        rows = self._read_all()
        if any(r["fio"] == student.fio for r in rows):
            return False
        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        self._write_all(rows)
        return True

    def find(self, substr: str) -> List[Student]:
        rows = self._read_all()
        return [
            Student.from_dict(r)
            for r in rows
            if substr.lower() in r["fio"].lower()
        ]

    def remove(self, fio: str) -> int:
        rows = self._read_all()
        initial_count = len(rows)
        rows = [r for r in rows if r["fio"] != fio]
        self._write_all(rows)
        return initial_count - len(rows)

    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
        updated = False
        for r in rows:
            if r["fio"] == fio:
                for key, value in fields.items():
                    if key not in self.HEADER:
                        raise ValueError(f"Недопустимое поле: {key}")
                    r[key] = str(value)
                updated = True
        if updated:
            self._write_all(rows)
        return updated
