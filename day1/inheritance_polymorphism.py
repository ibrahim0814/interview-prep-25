class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        return f"{self.name} is making a sound"
    
    def bark(self) -> str:
        return f"{self.name} is barking"

class Samoyed(Animal):
    def __init__(self, name: str, age: int):
        # call the super class constructor
        super().__init__(name, age)
    
    # example of polymorphism, we are overriding the bark method from the Animal class
    def bark(self) -> str:
        return f"{self.name} is barking like a Samoyed"

class GoldenRetriever(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def fetch_ability(self) -> int:
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 5

class Poodle(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
    
    def sheeding_amount(self) -> int:
        return 0

class Husky(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

class GoldenDoodle(GoldenRetriever, Poodle):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)


sammy: Samoyed = Samoyed(name="Sammy", age=5)
print(sammy.name)
print(sammy.age)
print(sammy.make_sound())
print(sammy.bark())

husky: Husky = Husky(name="Husky", age=3)
print(husky.name)
print(husky.age)
print(husky.make_sound())
print(husky.bark())
#we can't call the fetch_ability method because it is not defined in the Husky class

combo = GoldenDoodle(name="Combo", age=7)
print(combo.name)
print(combo.age)
print(combo.make_sound())
print(combo.bark())
print(combo.fetch_ability())
print(combo.sheeding_amount())