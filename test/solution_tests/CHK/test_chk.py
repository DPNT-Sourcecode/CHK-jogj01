from lib.solutions.CHK import checkout_solution_old
import pytest


@pytest.mark.parametrize("skus, expected_result", [
    (100, -1),
    ("", 0),
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 200),
    ("AAAAAAAA", 330),
    ("AAAAAAAAA", 380),
    ("AABCDAEE", 245),
    ("AABCDBAACDDD", 325),
    ("AABCDBA", 210),
    ("AABCDBAEE", 260),
    ("AABZTCDBA", -1),
    ("AACDAEE", 245),
    ("ABCDE", 155),
    ("ABCDEABCDE", 280),
    ("ABCa", -1),
    ("AxA", -1),
    ("B", 30),
    ("BEBEEE", 160),
    ("C", 20),
    ("D", 15),
    ("EEEEBB", 160),
    ("Z", -1),
])
def test_checkout(skus, expected_result):
    assert checkout_solution_old.checkout(skus) == expected_result