from typing import List

from lxml import etree

from models import ScientistQuery, Scientist
from .base import BaseStrategy


class DOMStrategy(BaseStrategy):

    def _tree(self) -> etree.Element:
        with open(self._filepath, "rb") as f:
            tree = etree.XML(f.read())
            return tree

    def _parse(self, element: etree.Element) -> Scientist:
        pass

    def all(self) -> List[Scientist]:
        tree = self._tree()
        return []

    def find(self, query: ScientistQuery) -> List[Scientist]:
        pass
