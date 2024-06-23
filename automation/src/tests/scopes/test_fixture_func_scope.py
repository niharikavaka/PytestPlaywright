import pytest 
# Purpose: Fixture runs once before and after each test function.

@pytest.fixture(scope="function")
def setup_teardown():
    print("Setup before function")
    yield
    print("Teardown after function")

def xtest_example1(setup_teardown):
    assert True

def xtest_example2(setup_teardown):
    assert True

      