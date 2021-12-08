import os.path

from exporter import TableExporter
from strategies.dom import DOMStrategy


class TestTableExporter:
    def test_default(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = DOMStrategy()
        scientists = strategy.all(filepath)

        html = TableExporter.render(scientists)
        assert len(html) > 0
