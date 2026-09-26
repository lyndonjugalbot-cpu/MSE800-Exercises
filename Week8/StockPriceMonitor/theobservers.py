class Observer:
    def update(self, price):
        pass

class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} received new stock price: {price}")

class Stock:
    def __init__(self):
        self.investors = []
        self.price = None

    def subscribe(self, investor):
        self.investors.append(investor)

    def notify(self):
        for investor in self.investors:
            investor.update(self.price)

    def set_price(self, price):
        self.price = price
        self.notify()