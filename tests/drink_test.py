import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Whiskey", 10)
        self.drink_2 = Drink("Beer", 10, 5)

    def test_drink_has_name(self):
        self.assertEqual("Whiskey", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(10, self.drink.price)

    def test_drink_unit__default(self):
        self.assertEqual(10, self.drink.unit)

    def test_drink_unit__custom_unit(self):
        self.assertEqual(5, self.drink_2.unit)
