from collections import Counter
from typing import List


class BigramCounter:
    def __init__(self, head, tails: List[str]):
        self._head = head
        self._counter = Counter(tails)

    def __str__(self):
        return f'Head: {self._head}\n' +\
                '\n'.join(f'Tail: {w:10s} Count: {c}' for w, c
                          in self._counter.most_common()) + '\n'
