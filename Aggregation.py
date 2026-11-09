class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, wheel_obj):
        self.wheel = wheel_obj  

    def check_wheels(self):
        print(f"Car is using {self.wheel.size}-inch wheels.")

my_wheel = Wheel(15)
my_car = Car(my_wheel)
my_car.check_wheels() 
