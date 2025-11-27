from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    encoding: кодировка файла ('utf-8' стоит по умолчанию, но можно выбрать 'cp1251' или другую).
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


import csv
from pathlib import Path
from typing import Iterable, Sequence


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        len_rows = len(rows[0])
        for element in rows:
            if len_rows != len(element):
                raise ValueError("Все строки должны иметь одинаковую длину")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
