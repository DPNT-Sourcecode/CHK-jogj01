from lib.solutions.HLO import hello_solution
import pytest


@pytest.mark.parametrize("friend_name, expected_result", [
    ("Robert", "Hello Robert!"),
    ("", "Please enter your friend's name."),
    ("1955489", "Hello 1955489!"),
])
def test_hello(friend_name, expected_result):
    assert hello_solution.hello(friend_name) == expected_result