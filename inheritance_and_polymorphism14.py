# Base class (Grandparent)
class Vehicle:
    def __init__(self, brand):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string.")
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")

# Intermediate class (Parent) inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call Vehicle's constructor
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        self.model = model
    def show_model(self):
        print(f"Model: {self.model}")

# Derived class (Child) inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call Car's constructor
        if not isinstance(battery_capacity, (int, float)) or battery_capacity <= 0:
            raise ValueError("Battery capacity must be a positive number.")
        self.battery_capacity = battery_capacity
    def show_details(self):
        # Access methods from parent and grandparent
        self.show_brand()
        self.show_model()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Example usage
if __name__ == "__main__":
    try:
        # Create an ElectricCar object
        tesla = ElectricCar("Tesla", "Model S", 100)
        tesla.show_details()
        print("\nAnother example:")
        tata_ev = ElectricCar("Tata", "Nexon EV", 40)
        tata_ev.show_details()
    except ValueError as e:
        print(f"Error: {e}")