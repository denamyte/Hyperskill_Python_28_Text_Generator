import re
from collections import defaultdict
from typing import List, Dict
from data import BigramCounter


def main():
    corpus = read_file(input())
    bigrams = convert_to_bigrams(corpus)
    while (cmd := input()) != 'exit':
        try:
            print(bigrams[cmd])
        except KeyError:
            print(f'Head: {cmd}')
            print('The requested word is not in the model.')


def read_file(name: str) -> List[str]:
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
    return re.split(r'\s', text.strip())


def convert_to_bigrams(corpus: List[str]) -> Dict[str, BigramCounter]:
    second_iter = iter(corpus)
    next(second_iter)
    dic = defaultdict(list)
    for h, t in zip(corpus, second_iter):
        dic[h].append(t)
    return {k: BigramCounter(k, v) for k, v in dic.items()}


if __name__ == '__main__':
    main()
