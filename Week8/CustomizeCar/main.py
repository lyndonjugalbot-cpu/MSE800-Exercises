from decoratorss import PremiumSoundSystemDecorator, LeatherSeatsDecorator, SunroofDecorator, GPSDecorator, Car


fully_loaded = PremiumSoundSystemDecorator(
    LeatherSeatsDecorator(
        (
            GPSDecorator(Car())
        )
    )
)
print(fully_loaded.description(), ":", fully_loaded.cost())
# Basic Car + GPS + Sunroof + Leather Seats + Premium Sound System : 28800