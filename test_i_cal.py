
# from calc import calculator
#
# def test_add():
#     assert calculator(1,10,5)==15
#
# def test_subtract():
#     assert calculator(2,15,10)==5
#
# def test_multi():
#     assert calculator(3,20,10)==200
#
# def test_devide():
#     assert calculator(4,15,5)==3

# File: test_calculator.py

from even import even_number  # 👈 logic import kar rahe

import pytest

@pytest.mark.parametrize("num", [2, 4, 6, 8, 10])
def test_even_numbers(num):
    assert even_number(num) == True

@pytest.mark.parametrize("num", [1, 3, 5, 7, 9])
def test_odd_numbers(num):
    assert even_number(num) == False


