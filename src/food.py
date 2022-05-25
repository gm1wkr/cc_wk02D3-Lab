class Food:
    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    def buy_food(self, customer, pub):
        # remove cash from C Wallet
        if customer.wallet >= self.price:
            customer.wallet -= self.price
            pub.till += self.price
            customer.drunk_level -= self.rejuvenation_level