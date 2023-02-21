from typing import List

from model import Model


def main():
    sentences = Model(read_file(input())).gen_sentences(10)
    print(*sentences, sep='\n')


def read_file(name: str) -> List[str]:
    with open(name, 'r', encoding='utf-8') as f:
        return f.read().replace(' .', '').strip().split()


if __name__ == '__main__':
    main()
