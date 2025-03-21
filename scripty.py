# Base class
class Animal:
    def move(self):
        """Default move method (to be overridden by subclasses)"""
        pass

# Animal Subclasses
class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

# Vehicle Base Class
class Vehicle:
    def move(self):
        """Default move method (to be overridden by subclasses)"""
        pass

# Vehicle Subclasses
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# List of objects with polymorphic behavior
objects = [Dog(), Bird(), Car(), Plane()]

# Loop through objects and call move() dynamically
for obj in objects:
    print(f"{obj.__class__.__name__}: {obj.move()}")
