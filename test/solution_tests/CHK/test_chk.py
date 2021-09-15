from solutions.CHK import checkout_solution


class TestChk():
    def test_illegal(self):
        assert checkout_solution.checkout("E") == -1

    def test_single(self):
        assert checkout_solution.checkout("C") == 20

    def test_multi(self):
        assert checkout_solution.checkout("CD") == 20 + 15

    def test_special_offer(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_multi_special_offer(self):
        assert checkout_solution.checkout("AAABB") == 130 + 45

    def test_multi_special_offer_and_others(self):
        assert checkout_solution.checkout("AAABBC") == 130 + 45 + 20