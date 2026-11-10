# Multilevel Inheritance Example in Python:
class Person:
    # Base class representing a person.
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.name = name.strip()
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    # Intermediate class inheriting from Person.
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        if not isinstance(employee_id, str) or not employee_id.strip():
            raise ValueError("Employee ID must be a non-empty string.")
        self.employee_id = employee_id.strip()
    def display_employee_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}")
class Manager(Employee):
    # Derived class inheriting from Employee.
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department must be a non-empty string.")
        self.department = department.strip()
    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department: {self.department}")
# Example usage
if __name__ == "__main__":
    try:
        # Taking user input
        name = input("Enter name: ").strip()
        age_input = input("Enter age: ").strip()
        emp_id = input("Enter employee ID: ").strip()
        dept = input("Enter department: ").strip()
        # Validate and convert age
        if not age_input.isdigit():
            raise ValueError("Age must be a positive integer.")
        age = int(age_input)
        # Create Manager object
        manager = Manager(name, age, emp_id, dept)
        print("\nManager Details:")
        manager.display_manager_info()
    except ValueError as e:
        print(f"Error: {e}")