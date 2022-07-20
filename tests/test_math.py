"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

#------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------

import pytest


#------------------------------------------------------------------------------------------------
#   A most basic test function
#------------------------------------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2 
    
    
"""
What command prints the current Python version?
    python --version

Conventionally, tests in a Python project belong under a directory named "test".
    true
    
What command does pytest used for making assertions?
    assert
    
What is the best command for running pytest test?
    python -m pytest
    
pytest treats all function in modules under the "tests" directory as test cases.
    false
"""

#------------------------------------------------------------------------------------------------
#   A most basic test function
#------------------------------------------------------------------------------------------------

"""
#Failed test case
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c
"""

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    
    """
    1. One Python test module can contain more than one test case function.
        true
        
    2. What symbol does pytest use in its reports to denote a passing test?
        .
        
    3. What symbol does pytest use in its reports to denote a failing test?
        F
        
    4. What types of exceptions will make a pytest test case fail?
        any type of exception
        
    5. By default, pytest will print test code snippets, failure reasons, and test result tallies for failed test cases.
        true
    """
    
#------------------------------------------------------------------------------------------------
#   A test function that verifies an exception
#------------------------------------------------------------------------------------------------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)
    """
    1. What is the purpose of "pytest.raises"?
    To verify that the code under test raises expected exceptions.
    
    2. "pytest.raises" must be imported from the pytest module.
    true
    
    3. "pytest.raises" does not look for exceptions based on type.
    false
    
    4. Why does "pytest.raises" need to be used with a "with" statement?
    The "with" statement executes additional "enter" and "exit" logic for handling raised exceptions.
    
    5. How can "pytest.raises" store the raised exception object for further assertions?
    Add an "as" clause to the end of the "with" statement to store the exception into a variable.
    """