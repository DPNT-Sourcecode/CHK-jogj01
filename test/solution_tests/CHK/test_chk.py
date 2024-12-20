from lib.solutions.CHK import checkout_solution
import pytest


@pytest.mark.parametrize("skus, expected_result", [
    ("A", 50),
    ("B", 30),
    ("C", 20),
    ("D", 15),
    ("Z", -1),
    (100, -1),
    ("", 0),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 200),
    ("AABCDBAACDDD", 325),
    ("AABCDBA", 210),
    ("AABZTCDBA", -1),
    ("ABCa", -1),
    ("AxA", -1),
    ("AACDAEE", 245),
    ("AABCDAEE", 245),
    ("AABCDBAEE", 260),
    ("ABCDE", 155),
    ("AAAAAAAA", 330),
    ("AAAAAAAAA", 380)

])
def test_checkout(skus, expected_result):
    assert checkout_solution.checkout(skus) == expected_result