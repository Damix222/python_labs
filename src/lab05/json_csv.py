import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.is_file():
        raise FileNotFoundError('файл не найден')

    with json_path.open(encoding='utf-8') as f:
        data = json.load(f)

    if len(data) == 0:
        raise ValueError('файл пустой')
    
    if not isinstance(data, list):
        raise ValueError('неверный тип файла')
    
    for element in data:
        if not isinstance(element, dict):
            raise ValueError('неверный тип файла')
        
    headers = list(data[0].keys())
    '''
    Порядок колонок как в 1 объекте 
    '''
    with csv_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  
        for row in data:
            row_data = {key: row.get(key, '') for key in headers}
            writer.writerow(row_data)

json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.is_file():
        raise FileNotFoundError('файл не найден')
    
    with csv_path.open(encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            raise ValueError('файл не содержит заголовка')
        data = list(r)
    if not data:
        raise ValueError('файл пуст')
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json') 