import pytest


@pytest.fixture()
def setup():
    print(" ---------------1111 method")
    yield
    print("After Every method 222--")


def test_method1(setup):
    print("test case 1")


def test_method2(setup):
    print("test case 2")
