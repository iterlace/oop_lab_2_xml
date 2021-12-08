import abc
from typing import List

from models import Scientist, ScientistQuery


class BaseStrategy(abc.ABC):

    def __init__(self, filepath: str):
        self._filepath = filepath

    @abc.abstractmethod
    def all(self) -> List[Scientist]:
        ...

    @abc.abstractmethod
    def find(self, query: ScientistQuery) -> List[Scientist]:
        ...
