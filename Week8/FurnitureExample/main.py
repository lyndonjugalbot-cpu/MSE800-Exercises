from Abstracts import ModernFurnitureFactory

#Client
factory = ModernFurnitureFactory()
chair = factory.create_chair()
sofa = factory.create_sofa()

chair.sit()
sofa.relax()