import os.path

from models import ScientistQuery
from strategies.bs4 import BS4Strategy


class TestBS4Strategy:
    def test_all(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = BS4Strategy()
        scientists = strategy.all(filepath)
        assert len(scientists) == 5

    def test_find(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = BS4Strategy()
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
        strategy = BS4Strategy()
        query = ScientistQuery(
            full_name="",
            faculty="",
            cathedra="",
            laboratory="",
            post="",
        )
        scientists = strategy.find(filepath, query)
        assert len(scientists) == 5
