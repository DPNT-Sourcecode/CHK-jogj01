from lib.solutions.HLO import hello_solution
import pytest


@pytest.mark.parametrize("friend_name, expected_result", [
    ("Robert", "Hello, World!"),
    ("", "Hello, World!"),
    ("1955489", "Hello, World!"),
])
def test_hello(friend_name, expected_result):
    assert hello_solution.hello(friend_name) == expected_result