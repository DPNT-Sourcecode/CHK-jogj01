from lib.solutions.CHK import checkout_solution
import pytest


@pytest.mark.parametrize("skus, expected_result", [
    ("A", 50),
    ("B", 30),
    ("C", 20),
    ("D", 15),
    ("", -1),
    ("Z", -1),
    ("AA", -1),
    (100, -1),
])
def test_checkout(skus, expected_result):
    assert checkout_solution.checkout(skus) == expected_result