"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

#------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------

from math import prod
import pytest


#------------------------------------------------------------------------------------------------
#   A most basic test function
#------------------------------------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2 
    
    
"""
Chapter 1
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
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    
    
    """
    Chapter 2
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

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)
    
    
    """
    Chapter 3
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
    
    # Multiplication test ideas
    
    # two positive integers
    # identity: multiply any number by 1
    # zero: multiply any number by 0
    # positive by a negative
    # negative by a negative
    # multiply floats
    """
    
    def test_multiply_two_positive_ints():
        assert 2 * 3 == 6
        
        
    def test_multiply_identity():
        assert 1 * 99 == 99
        
        
    def test_multiply_zero():
        assert 0 * 100 == 0 
        
        
    # DRY Principle: Don't Repeat Yourself!
    """
    
#------------------------------------------------------------------------------------------------
#   A parametrized test function
#------------------------------------------------------------------------------------------------

products = [
    (2, 3, 6),              # positive integers
    (1, 99, 99),            # identity
    (0, 99, 0),             # zero
    (3, -4, -12),           # positive by negative
    (-5, -5, 25),           # negative by negative
    (2.5, 6.7, 16.75)       # floats
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b , product):
    assert a * b == product 
    
"""
Chapter 4
1. What is an "equivalence class" for test case inputs?
    A unique kind of input that yields a unique kind of output.
    
2. What is the name of the pytest decorator for parametrized inputs?
    @pytest.mark.parametrize
    
3. What is the data format for passing pytest parameters?
    a list of parameter value tuples
    
4. pytest parameters may be strings as well as numbers.
    true
    
5. pytest parameters cannot be read from external files.
    false
"""