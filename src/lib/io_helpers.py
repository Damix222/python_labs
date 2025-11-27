import os
from pathlib import Path


def ensure_directory_exists(file_path):
    """Создает директорию, если она не существует"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def read_file(file_path):
    """Читает содержимое файла"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(file_path, content):
    """Записывает содержимое в файл"""
    ensure_directory_exists(file_path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
