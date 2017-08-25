import random
from . import type


class Vocabulary:
    def __init__(self, data: type.vocabulary_dict) -> None:
        self.__data = data

    def getRandomDict(self) -> type.identity:
        d = dict()

        for l in self.__data.values():
            d.update(random.choice(l))

        return d