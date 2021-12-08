from typing import List

from lxml import etree

from common import str2date
from models import Scientist, ScientistQuery

from .base import BaseStrategy


class DOMStrategy(BaseStrategy):
    def _tree(self, filepath: str) -> etree.Element:
        with open(filepath, "rb") as f:
            tree = etree.XML(f.read())
            return tree

    def _parse(self, element: etree.Element) -> Scientist:
        scientist = Scientist(
            full_name=element.find("full_name").text,
            faculty=element.find("faculty").text,
            cathedra=element.find("cathedra").text,
            laboratory=int(element.find("laboratory").text),
            post=element.find("post").text,
            post_start=str2date(element.find("post_start").text),
            post_end=str2date(element.find("post_end").text),
        )
        return scientist

    def all(self, filepath: str) -> List[Scientist]:
        nodes = self._tree(filepath).xpath("/scientists/scientist")
        scientists = [self._parse(node) for node in nodes]
        return scientists

    def find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        tree = self._tree(filepath)
        clauses = []
        for field, value in query.__dict__.items():
            clauses.append(f'{field}[contains(text(), "{value}")]')

        clause = " and ".join(clauses)
        nodes = tree.xpath(f"/scientists/scientist[{clause}]")
        scientists = [self._parse(node) for node in nodes]
        return scientists
