from dataclasses import dataclass


@dataclass
class Bigram:
    head: str
    tail: str

    def __str__(self):
        return f'Head: {self.head} Tail: {self.tail}'
