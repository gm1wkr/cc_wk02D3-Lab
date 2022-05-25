import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bob", 100, 19)

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(10)
        self.assertEqual(90, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(19, self.customer.age)


    def test_drunkenness_level(self):
        self.assertEqual(0, self.customer.drunk_level)