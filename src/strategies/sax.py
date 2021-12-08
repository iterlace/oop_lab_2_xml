from typing import List

from models import ScientistQuery, Scientist
from .base import BaseStrategy


class SAXStrategy(BaseStrategy):

    def __init__(self):
        super(SAXStrategy, self).__init__()

    def all(self, filepath: str) -> List[Scientist]:
        pass

    def find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        pass
