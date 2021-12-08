import os.path

import pytest

from strategies.dom import DOMStrategy


class TestDOMStrategy:

    def test_all(self, data_dir):
        filepath = os.path.join(data_dir, "sample1.xml")
        strategy = DOMStrategy(filepath)
        scientists = strategy.all()
        assert len(scientists) == 5
