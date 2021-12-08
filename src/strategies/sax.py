import xml.sax
from typing import Any, Dict, List, Optional

from common import str2date
from models import Scientist, ScientistQuery

from .base import BaseStrategy


class SAXStrategy(BaseStrategy):
    def __init__(self):
        super(SAXStrategy, self).__init__()

    def _find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        handler = SAXHandler(query)
        parser.setContentHandler(handler)
        parser.parse(filepath)
        return handler.matches

    def all(self, filepath: str) -> List[Scientist]:
        return self._find(filepath, ScientistQuery.empty())

    def find(self, filepath: str, query: ScientistQuery) -> List[Scientist]:
        return self._find(filepath, query)


class SAXHandler(xml.sax.handler.ContentHandler):
    fields = [
        "full_name",
        "faculty",
        "cathedra",
        "laboratory",
        "post",
        "post_start",
        "post_end",
    ]

    def __init__(self, query: ScientistQuery):
        super(SAXHandler, self).__init__()
        self.query = query
        self.current_data: Optional[Dict[str, Any]] = None
        self.current_field_name: Optional[str] = None
        self.current_field_value: Optional[str] = None
        self.matches: List[Scientist] = []

    def startElement(self, name, attrs):
        if name == "scientist":
            self.current_entry = Scientist.empty()
            self.current_data = {}
        elif name in self.fields:
            self.current_field_name = name
            self.current_field_value = ""

    def endElement(self, name):
        if name == "scientist":
            if self._validate(self.query, self.current_data):
                scientist = Scientist(
                    full_name=self.current_data["full_name"],
                    faculty=self.current_data["faculty"],
                    cathedra=self.current_data["cathedra"],
                    laboratory=int(self.current_data["laboratory"]),
                    post=self.current_data["post"],
                    post_start=str2date(self.current_data["post_start"]),
                    post_end=str2date(self.current_data["post_end"]),
                )
                self.matches.append(scientist)
            self.current_data = None
        elif name in self.fields:
            assert name == self.current_field_name
            self.current_data[name] = self.current_field_value
            self.current_field_name = None
            self.current_field_value = None

    def characters(self, chars):
        if not self.current_field_name:
            return
        self.current_field_value += chars

    @staticmethod
    def _validate(query: ScientistQuery, data: Dict[str, Any]):
        for field, value in query.__dict__.items():
            if not value:
                continue
            if value not in data.get(field, ""):
                return False
        return True
