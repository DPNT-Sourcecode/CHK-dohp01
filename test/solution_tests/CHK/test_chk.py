from solutions.CHK import checkout_solution


class TestChk():
    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_illegal(self):
        assert checkout_solution.checkout("z") == -1

    def test_single(self):
        assert checkout_solution.checkout("C") == 20

    def test_multi(self):
        assert checkout_solution.checkout("CCD") == 20 * 2 + 15

    def test_special_offer(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_special_offer_more(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_special_offer_triple(self):
        assert checkout_solution.checkout("AAAAAAAAAAAAAAA") == 200 * 3

    def test_special_offer_varied(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 200 + 130 + 50

    def test_multi_special_offer(self):
        assert checkout_solution.checkout("AAABB") == 130 + 45

    def test_multi_special_offer_and_others(self):
        assert checkout_solution.checkout("AAABBC") == 130 + 45 + 20

    def test_special_offer_one_free(self):
        assert checkout_solution.checkout("EEB") == 40 * 2

    def test_special_offer_one_free_again(self):
        assert checkout_solution.checkout("EEEB") == 40 * 3

    def test_special_offer_two_free(self):
        assert checkout_solution.checkout("EEEEBB") == 40 * 4

    def test_one_of_each_item(self):
        assert checkout_solution.checkout("ABCDE") == 50 + 30 + 20 + 15 + 40

    def test_two_of_each_item(self):
        assert checkout_solution.checkout("ABCDEABCDE") == 2*50 + 30 + 2*20 + 2*15 + 2*40

    def test_buy_two_get_one_free(self):
        assert checkout_solution.checkout("FFF") == 10 * 3 - 10

    def test_buy_four_get_two_free(self):
        assert checkout_solution.checkout("FFFFFF") == 10 * 6 - 10 * 2

    def test_buy_less_than_three_no_free(self):
        assert checkout_solution.checkout("FF") == 10 * 2

    def test_buy_three_get_only_one_free(self):
        assert checkout_solution.checkout("FFFF") == 10 * 4 - 10