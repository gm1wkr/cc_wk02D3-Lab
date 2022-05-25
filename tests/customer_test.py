import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bob", 100, 19)
        self.drunkard = Customer("Jimmy", 20, 20)
        self.drink = Drink("Gin", 5, 12)
        self.pub = Pub("White Horse", 1000)

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

    def test_increase_drunk_level(self):
        drunk_level = self.customer.increase_drunk_level(20)
        self.assertEqual(20, self.customer.drunk_level)

    def test_decrease_drunk_level(self):
        self.customer.increase_drunk_level(19)
        self.customer.decrease_drunk_level(9)
        self.assertEqual(10, self.customer.drunk_level)

    def test_increase_drunk_level__pass(self):
        drunk_level = self.customer.increase_drunk_level(self.drink.unit)
        self.assertEqual(12, self.customer.drunk_level)
    
    def test_is_customer_too_drunk__bladdered(self):
        self.drunkard.increase_drunk_level(205)
        is_too_drunk = self.pub.is_customer_too_drunk(self.drunkard)
        self.assertEqual(True, is_too_drunk)
    
    def test_is_customer_too_drunk__sober(self):
        is_too_drunk = self.pub.is_customer_too_drunk(self.customer)
        self.assertEqual(False, is_too_drunk)
