import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whiskey", 10)
        self.customer = Customer("Bob", 100, 19)
        self.customer_young = Customer("Jane", 100, 17)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_drink(self):
        # Get drink price
        drink_price = self.drink.price
        # take customer money
        self.customer.decrease_wallet(drink_price)
        # put money in till
        self.pub.increase_till(drink_price)

    def test_check_customer_age__pass(self):
        old_enough = self.pub.check_customer_age(self.customer.age)
        self.assertEqual(True, old_enough)

    def test_check_customer_age__fail(self):
        old_enough = self.pub.check_customer_age(self.customer_young.age)
        self.assertEqual(False, old_enough)

