from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine roaring!")