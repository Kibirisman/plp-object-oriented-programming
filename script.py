class Superhero:
    def __init__(self, name, alias, power, strength_level):
        """Initialize a superhero with basic attributes."""
        self.name = name
        self.alias = alias
        self.power = power
        self.__strength_level = strength_level  # Private attribute

    def introduce(self):
        """Introduce the superhero."""
        return f"I am {self.alias}, also known as {self.name}. My power is {self.power}!"

    def get_strength_level(self):
        """Encapsulated method to get strength level."""
        return f"{self.alias}'s strength level is {self.__strength_level}."

    def set_strength_level(self, level):
        """Encapsulated method to modify strength level."""
        if level > 0:
            self.__strength_level = level
        else:
            print("Strength level must be positive!")

# Subclass demonstrating inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, power, strength_level, flight_speed):
        """Initialize a flying superhero with additional attributes."""
        super().__init__(name, alias, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        """Method specific to flying superheroes."""
        return f"{self.alias} is flying at {self.flight_speed} mph!"

# Creating objects
hero1 = Superhero("Bruce Wayne", "Batman", "Martial Arts & Intelligence", 90)
hero2 = FlyingSuperhero("Clark Kent", "Superman", "Super Strength & Flight", 100, 500)

# Demonstrating functionality
print(hero1.introduce())
print(hero1.get_strength_level())

print(hero2.introduce())
print(hero2.fly())
print(hero2.get_strength_level())

# Updating strength level using encapsulation
hero1.set_strength_level(95)
print(hero1.get_strength_level())
