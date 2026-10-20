class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car_name):
        print(f"{self.name} is now driving the {car_name}.")

class Car:
    def __init__(self, model):
        self.model = model 
