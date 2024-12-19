from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("Robert") == "Hello Robert!"
        assert hello_solution.hello("") == "Please enter your friend's name."