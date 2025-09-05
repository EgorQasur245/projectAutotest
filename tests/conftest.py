import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope="module")  # т.к это модуль его достаточо написать один раз в каком нибудь тесте
def set_group():
    print("Enter system")
    yield
    print("Exit system")