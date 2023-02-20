import re
from typing import List

RE_ERROR = re.compile(r'(?<=\')\w+(?=Error)')


def main():
    corpus = read_file(input())
    print_stats(corpus)
    while (cmd := input()) != 'exit':
        try:
            print(corpus[int(cmd)])
        except Exception as e:
            print(f'{RE_ERROR.search(str(type(e))).group()} Error')


def read_file(name: str) -> List[str]:
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
    return re.split(r'\s', text.strip())


def print_stats(corpus: List[str]):
    print(f'''\
Corpus statistics
All tokens: {len(corpus)}
Unique tokens: {len(set(corpus))}
''')


if __name__ == '__main__':
    main()
