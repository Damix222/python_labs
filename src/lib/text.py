def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text

from re import *
def tokenize(text: str) -> list[str]:
    pattern = r'\b\w+(?:-\w+)*\b'
    return findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for element in tokens:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return dict(sorted(freq.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    items = list(freq.items())
    items.sort(key=lambda x: x[0])           
    items.sort(key=lambda x: x[1], reverse=True)  
    return items[:n]

if __name__ == '__main__':
    print('Вывод на задание normalize:')
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))

    print(("Вывод на задание tokenize:"))
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))

    print('Вывод на задание count_freq + top_n:')
    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
    print(top_n(count_freq(["a","b","a","c","b","a"])))
    print(top_n(count_freq(["bb","aa","bb","aa","cc"])))


