import collections
import random
import time
import uuid
from typing import Iterator, Generator, Any, Dict, KeysView, ValuesView, ItemsView
from . import type
from .vocabulary import Vocabulary


class RandomRecord(collections.Mapping):
    __template_prefix = "%%"
    __row = 0

    __template_cache = dict() # type: Dict[str, type.template]

    def __init__(self, jinja2_environment: type.environment, vocabulary: Vocabulary) -> None:
        self.__jinja2_environment = jinja2_environment
        self.__vocabulary = vocabulary
        self.next()

    def __get_template(self, template_string: str) -> type.template:
        if template_string not in self.__template_cache:
            self.__template_cache[template_string] = self.__jinja2_environment.from_string(template_string)

        return self.__template_cache[template_string]

    def __get_base_vars(self) -> type.identity:
        return dict(
            row = self.__row,
            uuid = str(uuid.uuid4()),
        )

    def next(self) -> None:
        self.__identity = self.__get_base_vars()
        self.__identity.update(self.__vocabulary.getRandomDict())
        self.__row += 1

    def __len__(self) -> int:
        return len(self.__identity)

    def __iter__(self) -> Iterator:
        return iter(self.__identity)

    def __getitem__(self, item: str) -> Any:
        value = self.__identity[item]
        while str(value).startswith(self.__template_prefix):
            value = self.__get_template(str(value)[len(self.__template_prefix):]).render(**self.__identity)

        return value

    def keys(self) -> KeysView:
        return self.__identity.keys()

    def values(self) -> ValuesView:
        return self.__identity.values()

    def items(self) -> ItemsView:
        return self.__identity.items()

    def generate(self, count: int, delay: float) -> Generator:
        counter = 0
        while count == 0 or count > counter:
            yield self
            time.sleep(delay)
            self.next()
            counter += 1


def random_record(jinja2_environment: type.environment, vocabulary: Vocabulary) -> RandomRecord:
    return RandomRecord(
        jinja2_environment,
        vocabulary
    )
