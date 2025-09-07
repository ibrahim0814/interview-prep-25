class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod # think of it like a helper function
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p1 = Person("Alice", 30)
print(Person.is_adult(20))       # True (static method)
p2 = Person.from_string("Bob-25")  # uses class method
print(p2.name, p2.age)           # Bob 25
