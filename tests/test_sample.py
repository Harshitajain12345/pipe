# tests/test_app.py
import pytest
from src.maths_operations import div , mult

# Test the add function
def test_div():
    assert div(6, 3) == 2
    assert div(10, 2) == 5
    assert div(9, 3) == 3

# Test the sub function
def test_mult():
    assert mult(5, 3) == 15
    assert mult(1, 1) == 1
    assert mult(0, 5) == 0