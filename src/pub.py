class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.refuses_drink = 100

        # should this be in the test file for testing?
        self.stock = {
            "Whiskey" : 100,
            "Gin": 150,
            "Beer": 200,
            "Pan_Galactic_Gargle_Blaster": 0
        }

    def increase_till(self, amount):
        self.till += amount


    def check_customer_age(self, age):
        return age >= 18

    def is_customer_too_drunk(self, customer):
        return self.refuses_drink <= customer.drunk_level

    def is_in_stock(self, drink):
        return drink.name in self.stock

    def reduce_stock(self, drink):
        if self.is_in_stock(drink) and self.stock[drink.name] >= 1:
            self.stock[drink.name] -= 1
    
    def sell_drink(self, customer, drink):
        if not self.check_customer_age(customer.age):
            return

        if self.is_customer_too_drunk(customer):
            return


        customer.decrease_wallet(drink.price)
        self.increase_till(drink.price)
        self.reduce_stock(drink)
        