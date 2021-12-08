import os

import pytest


@pytest.fixture(scope="session")
def data_dir():
    import tests

    tests_dir = os.path.dirname(os.path.realpath(tests.__file__))
    data_dir = os.path.join(tests_dir, "data")
    yield data_dir
