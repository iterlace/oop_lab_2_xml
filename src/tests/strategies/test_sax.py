import os.path

import pytest

from models import Scientist, ScientistQuery
from strategies.sax import SAXStrategy


class TestSAXStrategy:

    @pytest.mark.skip()
    def test_all(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy(filepath)
        scientists = strategy.all()
        assert len(scientists) == 5

    @pytest.mark.skip()
    def test_find(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy(filepath)
        query = ScientistQuery(
            full_name="",
            faculty="ФКНК",
            cathedra="",
            laboratory="",
            post="Доцент",
        )
        scientists = strategy.find(query)
        assert len(scientists) == 2

    @pytest.mark.skip()
    def test_find_empty_query(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = SAXStrategy(filepath)
        query = ScientistQuery(
            full_name="",
            faculty="",
            cathedra="",
            laboratory="",
            post="",
        )
        scientists = strategy.find(query)
        assert len(scientists) == 5
