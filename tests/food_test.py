import unittest

from src.food import Food
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestFood(unittest.TestCase):
    def setUp(self):
        self.chips = Food("Chips with Chips", 5.0, 10)
        self.pub = Pub("The Prancing Pony", 1000)
        self.drink = Drink("Whiskey", 10)
        self.customer = Customer("Bob", 100, 20)
        self.customer_poor = Customer("Mary", 1, 20)

    def test_food_has_name(self):
        self.assertEqual("Chips with Chips", self.chips.name)

    def test_food_has_price(self):
        self.assertEqual(5.0, self.chips.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(10, self.chips.rejuvenation_level)

    def test_buy_food__okay(self):        
        self.chips.buy_food(self.customer, self.pub)
        self.customer.drunk_level = 20
        self.chips.buy_food(self.customer, self.pub)

        self.assertEqual(90, self.customer.wallet)
        self.assertEqual(1010, self.pub.till)
        self.assertEqual(10, self.customer.drunk_level)

    def test_buy_food__no_cash(self):        
        self.chips.buy_food(self.customer_poor, self.pub)
        self.chips.buy_food(self.customer_poor, self.pub)

        self.assertEqual(1, self.customer_poor.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(0, self.customer_poor.drunk_level)