import coins

class Wallet:
    def __init__(self):
        self.money = self.fill_wallet()

    def fill_wallet(self):
        """Method will fill wallet's money list with certain amount of each type of coin when called."""
        money = []
        for _ in range(8):
            money.append(coins.Quarter())
        for _ in range(10):
            money.append(coins.Dime())
        for _ in range(20):
            money.append(coins.Nickel())
        for _ in range(50):
            money.append(coins.Penny())
        return money