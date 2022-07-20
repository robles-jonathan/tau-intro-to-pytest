"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

#------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator


#------------------------------------------------------------------------------------------------
#   Fixtures
#------------------------------------------------------------------------------------------------

@pytest.fixture
def accum():
    return Accumulator()


#------------------------------------------------------------------------------------------------
#   Test
#------------------------------------------------------------------------------------------------


def test_accumulator_init(accum):
    assert accum.count == 0
    
    
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1
    
    
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3
    
    
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2
    
    
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10
        
        
"""
1. What are "unit tests"?
    Small tests that directly cover "units of work" like functions and methods
    
2. What file turns a regular directory into a package in a Python project?
__init__.py

3. pytest can run tests from multiple modules in the same Python project.
true

4. Which of the following lines represents an "Arrange" step?
accum = Accumulator()

5. Which of the following lines represents an "Assert" step?
assert accum.count == 0
"""


"""
1. In pytest, what is a fixture?
    A function that handles setup and cleanup operations for a test case.
    
2. What is the name of the decorator used for defining functions as fixtures?
    @pytest.fixture
    
3. Fixtures cover the "Act" phase of "Arrange-Act-Assert".
    false
    
4. To share fixtures between test modules, where should the fixtures be located?
    In a "conftest.py" module under the "tests" directory.
    
5. A test case cannot use multiple fixtures.
    false
    
6. A fixture can provide both setup and cleanup logic by using a yield statement.
    true
"""