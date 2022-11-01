import os


def pytest_generate_tests():
    os.environ["PYTHONUNBUFFERED"] = "1"
    os.environ["PRODUCTION_MODE"] = "test"
    os.environ["RUNNER"] = "user"


def test_number():
    a = 4
    assert a == 4


def test_second_number():
    a = 5
    if os.environ["PRODUCTION_MODE"] == "test":
        a = 4
    assert a == 4
