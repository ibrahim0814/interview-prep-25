class Person:
    def __init__(self, name: str, age: int, gender: str ):
        # these are private attributes, so they are not accessible outside the class
        self.__name = name
        self.__age = age
        self.__gender = gender

    # notice how the method names are the same as the attribute names
    # this is a property decorator, it is used to get the attribute value
    @property
    def Name(self) -> str:
        return self.__name
    
    @property
    def Age(self) -> int:
        return self.__age
    
    @property
    def Gender(self) -> str:
        return self.__gender            

    @Name.setter
    def Name(self, name: str) -> None:
        self.__name = name

    @Age.setter
    def Age(self, age: int) -> None:
        self.__age = age
    
    @Gender.setter
    def Gender(self, gender: str) -> None:
        self.__gender = gender


person = Person(name="John", age=20, gender="Male")

# we have to use the property decorator to get the attribute value
print(person.Name)
print(person.Age)
print(person.Gender)

# we have to use the property decorator to set the attribute value
person.Name = "Jane"
person.Age = 21
person.Gender = "Female"
print(person.Name)
print(person.Age)
print(person.Gender)
