import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True

def test_new_index_function():
    assert index.new_index_function() == False




