class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.refuses_drink = 100
    
    def increase_till(self, amount):
        self.till += amount


    def check_customer_age(self, age):
        return age >= 18

    def is_customer_too_drunk(self, customer):
        return self.refuses_drink <= customer.drunk_level