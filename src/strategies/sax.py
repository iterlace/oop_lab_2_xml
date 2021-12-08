from typing import List

from models import ScientistQuery, Scientist
from .base import BaseStrategy


class SAXStrategy(BaseStrategy):

    def __init__(self, filepath: str):
        super(SAXStrategy, self).__init__(filepath)

    def all(self) -> List[Scientist]:
        pass

    def find(self, query: ScientistQuery) -> List[Scientist]:
        pass
