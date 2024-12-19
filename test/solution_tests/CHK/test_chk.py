from lib.solutions.CHK import checkout_solution
import pytest


@pytest.mark.parametrize("skus, expected_result", [
    ("Robert", "Hello, Robert!"),
    ("", "Hello, World!"),
    ("1955489", "Hello, 1955489!"),
])
def test_hello(skus, expected_result):
    assert checkout_solution.checkout(skus) == expected_result