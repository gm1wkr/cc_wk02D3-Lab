class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunk_level = 0

    def decrease_wallet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount

    def increase_drunk_level(self, unit):
        self.drunk_level += unit
    # def buy_drink