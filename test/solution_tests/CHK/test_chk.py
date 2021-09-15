from solutions.CHK import checkout_solution


class TestChk():
    def test_sum(self):
        assert checkout_solution.compute(1, 2) == 3
