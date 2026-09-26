class Pizza:
    def prepare(self):
        print("Preparing Pizza!")

class Burger:
    def prepare(self):
        print("Preparing Burger!")

class Pasta:
    def prepare(self):
        print("Preparing Pasta")

class OrderFactory:

    @staticmethod
    def create_order(order):
        if order == "Pizza":
            return Pizza()
        elif order == "Burger":
            return Burger()
        elif order == "Pasta":
            return Pasta()
        else:
            raise ValueError("Invalid Order!")



def main():

    order = OrderFactory.create_order("Pizza")
    order.prepare()

if __name__ == '__main__':
    main()