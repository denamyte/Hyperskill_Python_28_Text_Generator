import random
import string
from collections import defaultdict
from typing import List, Dict
from data import BigramCounter


class Model:
    def __init__(self, corpus: List[str]):
        self._corpus = corpus
        self._first_tokens = self._gen_first_tokens()
        self._bigrams = self._preprocess_data()

    def _preprocess_data(self) -> Dict[str, BigramCounter]:
        second_iter = iter(self._corpus)
        next(second_iter)
        dic = defaultdict(list)
        for h, t in zip(self._corpus, second_iter):
            dic[h].append(t)
        return {k: BigramCounter(k, v) for k, v in dic.items()}

    def gen_sentences(self, sent_count: int) -> List[str]:
        return [self._gen_sentence() for _ in range(sent_count)]

    def _gen_sentence(self) -> str:
        tokens = [random.choice(self._first_tokens)]
        count = 4
        while count > 0 or tokens[-1][-1] not in '.!?':
            count -= 1
            mc = self._bigrams[tokens[-1]].most_common
            tokens.append(random.choices(*zip(*mc), k=1)[0])
        return ' '.join(tokens)

    def _gen_first_tokens(self) -> List[str]:
        return [x for x in self._corpus if x[0].isupper()
                and x[-1] not in string.punctuation]
