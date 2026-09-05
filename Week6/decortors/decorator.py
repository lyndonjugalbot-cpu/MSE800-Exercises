import time

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.func.__name__} has been called {self.count} times.")
        return self.func(*args, **kwargs)



def timing_decorator(time_unit):
    def decorator(func):
        def wrapper():
            start_time = time.time()
            result = func()
            end_time = time.time()
            print(f"time taken: {end_time - start_time} / {time_unit}")
            return result
        return wrapper
    return decorator   

def add_sprinkles(func):
    def wrapper():
        print("You added sprinkles to your ice cream!")
        return func()
    return wrapper

@CallCounter
@add_sprinkles
@timing_decorator("seconds")
def get_ice_cream():
    print("Here's your ice cream.")




def main():
    get_ice_cream()

if __name__ == "__main__":
    main()