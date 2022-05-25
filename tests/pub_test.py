import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whiskey", 10)
        self.drink_not_found = Drink("Pan_Galactic_Gargle_Blaster", 90)
        self.customer = Customer("Zaphod Beeblebrox", 100, 19)
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

# Extensions
    def test_pub_has_stock_dict(self):
        self.assertEqual(isinstance(self.pub.stock, dict), True)

    def test_pub_has_price_dict(self):
        self.assertEqual(isinstance(self.pub.drink_price, dict), True)
    
    def test_is_in_stock__true(self):
        self.assertEqual(True, self.pub.is_in_stock(self.drink))

    def test_reduce_stock__has_stock(self):
        self.pub.reduce_stock(self.drink)
        self.assertEqual(99, self.pub.stock["Whiskey"])

    def test_reduce_stock__no_stock(self):
        self.pub.reduce_stock(self.drink_not_found)
        self.assertEqual(0, self.pub.stock["Pan_Galactic_Gargle_Blaster"])
  

    def test_get_stock(self):
        self.pub.reduce_stock(self.drink)
        self.assertEqual(99, self.pub.stock["Whiskey"])
        self.assertEqual(200, self.pub.stock["Beer"])
        self.assertEqual(150, self.pub.stock["Gin"])

    def test_sell_drink__okay(self):
        self.pub.till = 100
        self.assertEqual(100, self.pub.till)
        self.pub.sell_drink(self.customer, self.drink)
        self.assertEqual(True, self.pub.check_customer_age(self.customer.age))
        self.assertEqual(False, self.pub.is_customer_too_drunk(self.customer))
        self.assertEqual(90, self.customer.wallet)
        self.assertEqual(110, self.pub.till)

    def test_sell_drink__too_young(self):
        self.pub.till = 100
        self.pub.sell_drink(self.customer_young, self.drink)
        self.assertEqual(False, self.pub.check_customer_age(self.customer_young.age))
        self.assertEqual(100, self.customer_young.wallet)
        self.assertEqual(100, self.pub.till)

    def test_get_total_stock_value(self):
        self.assertEqual(3650, self.pub.get_total_stock_value())