import argparse
import sys
from pathlib import Path
from lib.text import normalize, tokenize, count_freq, top_n

def read_file_lines(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError('Файл не найден') 
    if not path.is_file():
        raise ValueError('не является файлом')
    try:
        with path.open(encoding='utf-8') as f:
            return f.readlines()
    except UnicodeDecodeError:
        raise ValueError(f'Невозможно прочитать файл (кодировка не UTF-8)')

def cat_command(input_file, number_lines):
    try:
        lines = read_file_lines(input_file)
        for i, line in enumerate(lines, start=1):
            if number_lines:
                print(f"{i}\t{line.rstrip()}")
            else:
                print(line.rstrip())
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def stats_command(input_file, top_count):
    if top_count <= 0:
        print("top_count должен быть положительным числом", file=sys.stderr)
        sys.exit(1)
    try:
        lines = read_file_lines(input_file)
    except (FileNotFoundError, ValueError) as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    text = ' '.join(lines)
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    most_common = top_n(freq, n=top_count)
    print(f"Top {top_n} words:")
    for word, count in most_common:
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI утилиты для обработки текста")
    subparsers = parser.add_subparsers(dest='command', required=True)

    cat_parser = subparsers.add_parser('cat', help='Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True, help='Входной файл')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    stats_parser = subparsers.add_parser('stats', help='Частоты слов в тексте')
    stats_parser.add_argument('--input', required=True, help='Входной текстовый файл')
    stats_parser.add_argument('--top', type=int, default=5, help='Сколько показать топ слов (по умолчанию 5)')

    args = parser.parse_args()

    if args.command == 'cat':
        cat_command(args.input, args.n)
    elif args.command == 'stats':
        stats_command(args.input, args.top)
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main() 