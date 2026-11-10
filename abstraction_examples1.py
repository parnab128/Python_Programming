from abc import ABC, abstractmethod
# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        # Abstract method - must be implemented by subclasses
        pass
    @abstractmethod
    def stop_engine(self):
        pass
# Concrete class implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
    def stop_engine(self):
        print("Car engine stopped.")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")
    def stop_engine(self):
        print("Bike engine stopped.")
# Using the classes
def operate_vehicle(vehicle: Vehicle):
    if not isinstance(vehicle, Vehicle):
        raise TypeError("Expected a Vehicle instance")
    vehicle.start_engine()
    vehicle.stop_engine()
# Example usage
if __name__ == "__main__":
    car = Car()
    bike = Bike()
    operate_vehicle(car)
    operate_vehicle(bike)