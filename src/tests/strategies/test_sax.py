import os.path

from models import ScientistQuery
from strategies.sax import SAXStrategy


class TestSAXStrategy:
    def test_all(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy()
        scientists = strategy.all(filepath)
        assert len(scientists) == 5

    def test_find(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy()
        query = ScientistQuery(
            full_name="",
            faculty="ФКНК",
            cathedra="",
            laboratory="",
            post="Доцент",
        )
        scientists = strategy.find(filepath, query)
        assert len(scientists) == 2

    def test_find_empty_query(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy()
        query = ScientistQuery.empty()
        scientists = strategy.find(filepath, query)
        assert len(scientists) == 5
