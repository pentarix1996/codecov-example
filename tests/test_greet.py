import pytest
from methods import tested, no_tested


@pytest.fixture
def name() -> str:
    return "Antonio"


def test_greet(name) -> None:
    assert tested.greet(name) == "Hello Antonio"


def test_Othergreet(name) -> None:
    assert no_tested.noTestedGreet(name) == "Hello Antonio"


def test_hello() -> None:
    assert tested.sayHello() == "Hello world!"


