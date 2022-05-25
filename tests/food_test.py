import unittest

from src.food import Food
from src.customer import Customer
# from src.drink import Drink
# from src.pub import Pub

class TestFood(unittest.TestCase):
    def setUp(self):
        self.chips = Food("Chips with Chips", 2.5, 20)

    def test_food_has_name(self):
        self.assertEqual("Chips with Chips", self.chips.name)

    def test_food_has_price(self):
        self.assertEqual(2.5, self.chips.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(20, self.chips.rejuvenation_level)
