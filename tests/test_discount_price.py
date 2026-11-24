
import unittest

from src.testdiscount import calculate_price


class PriceCalculatorTests(unittest.TestCase):

    def test_standard_customer_gets_no_discount(self):
        self.assertEqual(calculate_price(100, "STANDARD"), 100)

    def test_vip_customer_gets_10_percent_discount(self):
        self.assertEqual(calculate_price(100, "VIP"), 90)

    def test_zero_price_is_valid(self):
        self.assertEqual(calculate_price(0, "VIP"), 0)

    
    def test_zero_price_is_valid(self):
        self.assertEqual(calculate_price(0, "STANDARD"), 0)

    def test_negative_price_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_price(-50, "VIP")

   
if __name__ == "__main__":
    unittest.main()
