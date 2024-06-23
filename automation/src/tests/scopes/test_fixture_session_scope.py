# content of conftest.py
import pytest

@pytest.fixture(scope="session")
def setup_teardown():
    print("Setup once per session")
    yield
    print("Teardown once per session")

# content of test_session.py
def xtest_example1(setup_teardown):
    assert True

def xtest_example2(setup_teardown):
    assert True
