from abc import ABC, abstractmethod

#The Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def relax(self):
        pass


#concrete products
class ModernChair(Chair):
    def sit(self):
        print("Sitting on a modern chair")

class ModernSofa(Sofa):
    def relax(self):
        print("Relaxing on a modern sofa")


#Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

#Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()
