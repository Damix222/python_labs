import argparse
import sys
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def file_exists_or_exit(filepath):
    path = Path(filepath)
    if not path.exists():
        print('файл не найден', file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f'не является файлом', file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных: JSON, CSV, XLSX")
    subparsers = parser.add_subparsers(dest='cmd')

    p1 = subparsers.add_parser('json2csv', help='Конвертация JSON в CSV')
    p1.add_argument('--in', dest='input', required=True, help='Входной JSON файл')
    p1.add_argument('--out', dest='output', required=True, help='Выходной CSV файл')

    p2 = subparsers.add_parser('csv2json', help='Конвертация CSV в JSON')
    p2.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p2.add_argument('--out', dest='output', required=True, help='Выходной JSON файл')

    p3 = subparsers.add_parser('csv2xlsx', help='Конвертация CSV в XLSX')
    p3.add_argument('--in', dest='input', required=True, help='Входной CSV файл')
    p3.add_argument('--out', dest='output', required=True, help='Выходной XLSX файл')

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv':
            json_to_csv(args.input, args.output)
            print(f'конвертация JSON в CSV выполнена: {args.output}')
        elif args.cmd == 'csv2json':
            csv_to_json(args.input, args.output)
            print(f'конвертация CSV в JSON выполнена:  {args.output}')
        elif args.cmd == 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
            print(f'конвертация CSV в XLSX выполнена: : {args.output}')
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print('ошибка конвертации файла', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()