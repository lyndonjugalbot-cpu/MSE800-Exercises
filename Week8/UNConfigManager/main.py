from config import config1, config3, config2

config1.set_config("Yoobee Colleges", "2026", "Sem1")

#config 2 and 3 can see what has been set to config1
config2.display_config()
config3.display_config()


print(config1 is config2) #True
print(config2 is config3) #True
print(config3 is config1) #True