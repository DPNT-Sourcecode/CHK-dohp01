from solutions.CHK import checkout_solution


class TestChk():
    def test_illegal(self):
        assert checkout_solution.checkout("E") == -1

    def test_(self):
        assert checkout_solution.checkout("C") == -1
