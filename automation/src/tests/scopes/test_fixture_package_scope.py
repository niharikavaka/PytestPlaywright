# Purpose: Fixture runs once per package.

import pytest

@pytest.fixture(scope="package")
def setup_teardown():
    print("Setup once per package")
    yield
    print("Teardown once per package")

# content of test_package.py
def xtest_example1(setup_teardown):
    assert True

def xtest_example2(setup_teardown):
    assert True
