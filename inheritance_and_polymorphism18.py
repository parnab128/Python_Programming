class Engine:
    def start_engine(self):
        return "Engine started."
class Electricsystem:
    def check_battery(self):
        return "Battery fully charged."
# Inheriting from both Engine and Electricsystem
class HybridCar(Engine, Electricsystem):
    def drive(self):
        return "Car is moving smoothly."
# Usage
my_car=HybridCar()
print(my_car.start_engine()) # From Engine
print(my_car.check_battery()) # From Electricsystem
print(my_car.drive()) # From HybridCar