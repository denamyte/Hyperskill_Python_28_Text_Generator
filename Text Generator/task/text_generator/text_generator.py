import re
from typing import List
from data import Bigram

RE_ERROR = re.compile(r'(?<=\')\w+(?=Error)')


def main():
    corpus = read_file(input())
    bigrams = convert_to_bigrams(corpus)
    print(f'Number of bigrams: {len(bigrams)}\n')
    while (cmd := input()) != 'exit':
        try:
            print(bigrams[int(cmd)])
        except Exception as e:
            print(f'{RE_ERROR.search(str(type(e))).group()} Error ' * 2)


def read_file(name: str) -> List[str]:
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
    return re.split(r'\s', text.strip())


def convert_to_bigrams(corpus: List[str]) -> List[Bigram]:
    second_iter = iter(corpus)
    next(second_iter)
    return [Bigram(*z) for z in zip(corpus, second_iter)]


if __name__ == '__main__':
    main()
