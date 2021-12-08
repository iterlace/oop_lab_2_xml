import os.path

import pytest

from models import Scientist, ScientistQuery
from strategies.dom import DOMStrategy
from exporter import TableExporter


class TestTableExporter:

    def test_default(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = DOMStrategy()
        scientists = strategy.all(filepath)

        html = TableExporter.render(scientists)
        assert len(html) > 0
