from typing import List

import bs4

from models import ScientistQuery, Scientist
from common import str2date
from .base import BaseStrategy


class BS4Strategy(BaseStrategy):

    def _tree(self, filepath: str) -> bs4.BeautifulSoup:
        with open(filepath, "r") as f:
            tree = bs4.BeautifulSoup(f.read(), "xml")
            return tree

    def _parse(self, element: bs4.element.Tag) -> Scientist:
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
        tree = self._tree(filepath)
        nodes = tree.find("scientists").find_all("scientist")
        scientists = [self._parse(node) for node in nodes]
        return scientists

    def find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        tree = self._tree(filepath)
        root = tree.find("scientists")
        scientists = []
        for node in root.find_all("scientist"):
            for field, value in query.__dict__.items():
                if not value:
                    continue
                # TODO: maybe use "==" instead of "in"?
                if value not in node.find(field).text:
                    break
            else:
                scientists.append(self._parse(node))
        return scientists
