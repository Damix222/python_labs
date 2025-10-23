from src.lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n
import sys

def main(input_path: str = 'data/input.txt', output_path: str = 'data/report.csv', encoding: str = 'utf-8'):
    try:
        text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print('файл не найден')
        sys.exit(1)
    except UnicodeDecodeError:
        print('неправильная кодировка')
        sys.exit(1)
    '''
sys.exit(1) интерпретатор сразу завершает работу 
Значение аргумента (1):
Код возврата 1 означает, что программа завершилась с ошибкой.
Код возврата 0 означет успешное завершение программы.
    '''
    freq = count_freq(tokenize(normalize(text)))
    sorted_freq= top_n(count_freq(tokenize(normalize(text))))
    rows = sorted_freq
    header = ("word", "count")
    if rows:
        write_csv(rows, output_path, header=header)
    else:
        write_csv([], output_path, header=header)

    total_words = sum(freq.values())
    unique_words = len(freq)
    top_5 = sorted_freq[:5]

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_5:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
