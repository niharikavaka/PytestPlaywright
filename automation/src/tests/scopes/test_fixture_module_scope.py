import pytest

@pytest.fixture(scope="module")
def setup_teardown():
    print("Setup once per module")
    yield
    print("Teardown once per module")

def xtest_module(set_up_tear_down):
    assert True

def xtest_example2(setup_teardown):
    assert True