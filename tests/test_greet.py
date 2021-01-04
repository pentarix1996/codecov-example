import pytest
from methods import main


@pytest.fixture
def name() -> str:
    return "Antonio"


def test_greet(name) -> None:
    assert main.greet(name) == "Hello Antonio"


def test_hello() -> None:
    assert main.sayHello() == "Hello world!"
