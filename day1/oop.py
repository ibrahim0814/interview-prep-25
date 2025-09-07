class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already on")
            return
        self.turned_on = True
        print(f"{self.brand} microwave is turning on")
    
    def turn_off(self) -> None:
        if not self.turned_on:
            print(f"{self.brand} microwave is already off")
            return
        self.turned_on = False
        print(f"{self.brand} microwave is turning off")

    def run(self, seconds: int) -> None:
        if not self.turned_on:
            print(f"{self.brand} microwave is not on")
            return
        print(f"{self.brand} microwave is running for {seconds} seconds")

    # dunder method for addition (magic method)
    def __add__(self, other: 'Microwave') -> 'Microwave':
        return Microwave(brand=f"{self.brand} + {other.brand}", power_rating=f"{self.power_rating} + {other.power_rating}")

    # dunder method for string representation, important for printing the object
    def __str__(self) -> str:
        return f"{self.brand} microwave with power rating {self.power_rating}"

    #dunder method for representation, important for debugging
    def __repr__(self) -> str:
        return f"Microwave(brand={self.brand}, power_rating={self.power_rating})"

    # dunder method for equality
    def __eq__(self, other):
        return self.brand == other.brand and self.power_rating == other.power_rating

# instance of the Microwave class
smeg: Microwave = Microwave(brand="Smeg", power_rating="1000W")
smeg.turn_on()
smeg.run(seconds=10)
smeg.turn_off()
smeg.run(seconds=10)

bosch: Microwave = Microwave(brand="Bosch", power_rating="1500W")
bosch.turn_on()
bosch.run(seconds=10)
bosch.turn_off()
bosch.run(seconds=10)

combined: Microwave = smeg + bosch

print(combined)
print(repr(combined))
