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
#   Test
#------------------------------------------------------------------------------------------------


def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0
    
    
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1
    
    
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3
    
    
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2
    
    
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
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