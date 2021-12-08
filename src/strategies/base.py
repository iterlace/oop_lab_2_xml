import abc
from typing import List

from models import Scientist, ScientistQuery


class BaseStrategy(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def all(self, filepath: str) -> List[Scientist]:
        ...

    @abc.abstractmethod
    def find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        ...
