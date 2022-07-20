"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

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