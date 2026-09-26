class Car:
    def cost(self):
        return 25000

    def description(self):
        return "Basic Car"


class CarDecorator:
    def __init__(self, car):
        self.car = car

    def cost(self):
        return self.car.cost()

    def description(self):
        return self.car.description()


class GPSDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 500

    def description(self):
        return self.car.description() + " + GPS"


class SunroofDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1000

    def description(self):
        return self.car.description() + " + Sunroof"


class LeatherSeatsDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1500

    def description(self):
        return self.car.description() + " + Leather Seats"


class PremiumSoundSystemDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 800

    def description(self):
        return self.car.description() + " + Premium Sound System"