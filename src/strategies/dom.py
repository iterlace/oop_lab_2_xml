from typing import List
import datetime as dt

from lxml import etree

from models import ScientistQuery, Scientist
from common import str2date
from .base import BaseStrategy


class DOMStrategy(BaseStrategy):

    def _tree(self) -> etree.Element:
        with open(self._filepath, "rb") as f:
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

    def all(self) -> List[Scientist]:
        nodes = self._tree().xpath("/scientists/scientist")
        scientists = [self._parse(node) for node in nodes]
        return scientists

    def find(self, query: ScientistQuery) -> List[Scientist]:
        tree = self._tree()
        clauses = []
        for field, value in query.__dict__.items():
            clauses.append(f"{field}[contains(text(), \"{value}\")]")

        clause = " and ".join(clauses)
        nodes = tree.xpath(f"/scientists/scientist[{clause}]")
        scientists = [self._parse(node) for node in nodes]
        return scientists
