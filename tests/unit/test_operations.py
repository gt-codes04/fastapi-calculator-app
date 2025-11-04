import math
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app import operations as op

def test_add_basic():
    assert op.add(2, 3) == 5

def test_sub_negative():
    assert op.sub(2, 5) == -3

def test_mul_zero():
    assert op.mul(10, 0) == 0

def test_mul_floats():
    assert math.isclose(op.mul(2.5, 4.2), 10.5, rel_tol=1e-9)

def test_div_basic():
    assert op.div(10, 2) == 5

def test_div_float():
    assert math.isclose(op.div(3, 2), 1.5, rel_tol=1e-9)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        op.div(1, 0)
