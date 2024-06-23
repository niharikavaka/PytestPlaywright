import pytest

# Purpose: Fixture runs once before and after all test methods in a class.

@pytest.fixture(scope="class")
def setup_teardown():
    print("Setup before class")
    yield
    print("Teardown after class")

class TestClass:
    def xtest_example1(self, setup_teardown):
        assert True

    def xtest_example2(self, setup_teardown):
        assert True
        
