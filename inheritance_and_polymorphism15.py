""" Below is an implementation of a multi-level inheritance scenario in Python, where a base
class Vehicle has an attribute type. A derived class Car inherits from Vehicle, and another
class ElectricCar inherits from Car, adding a battery attribute"""

# Base class
class Vehicle:
   def __init__(self, vehicle_type):
       self.type = vehicle_type
   def display_type(self):
       print(f"Vehicle Type: {self.type}")
# Derived class
class Car(Vehicle):
   def __init__(self, vehicle_type, brand):
       super().__init__(vehicle_type)
       self.brand = brand
   def display_car_info(self):
       print(f"Car Brand: {self.brand}")
# Further derived class
class ElectricCar(Car):
   def __init__(self, vehicle_type, brand, battery_capacity):
       super().__init__(vehicle_type, brand)
       self.battery = battery_capacity
   def display_electric_car_info(self):
       print(f"Battery Capacity: {self.battery} kWh")
# Example usage
electric_car = ElectricCar("Electric", "Tesla", 75)
electric_car.display_type() # From Vehicle class
electric_car.display_car_info() # From Car class
electric_car.display_electric_car_info() # From ElectricCar class