class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.refuses_drink = 100

        # should this be in the test file for testing?
        self.stock = {
            "Whiskey" : 100,
            "Gin": 150,
            "Beer": 200
        }

    def increase_till(self, amount):
        self.till += amount


    def check_customer_age(self, age):
        return age >= 18

    def is_customer_too_drunk(self, customer):
        return self.refuses_drink <= customer.drunk_level

    def reduce_stock(self,drink):
        self.stock[drink.name] -= 1
    
    def sell_drink(self, customer, drink):
        # check customer age
        self.check_customer_age(customer.age)

        # check not too drunk
        self.is_customer_too_drunk(customer)

        # take money from customer if available
        customer.decrease_wallet(drink.price)
        
        # put money in till
        self.increase_till(drink.price)

        # reduce stock count

        pass