import pytest
from methods import main


@pytest.fixture
def name() -> str:
    return "Antonio"


def test_hello(name) -> None:
    assert main.greet(name) == "Hello Antonio"
