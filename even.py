# def even_number(number):
#     return number%2==0
#
# print(even_number(12))

import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("n", [2, 4, 6, 8, 10])
def test_even_numbers(n):
    assert is_even(n) == True

