class Person:
    def __init__(self, name: str, age: int, gender: str ):
        # public attribute
        # we can access the attribute outside the class
        self.name = name
  
        # protected attribute
        # we can access the attribute outside the class although not recommended
        self._age = age

        # private attribute
        # we can't access the attribute outside the class
        self.__gender = gender



my_person = Person(name="John", age=20, gender="Male")
print(my_person.name)
print(my_person._age)
# print(my_person.__gender) # this will raise an AttributeError
# we can access the protected attribute outside the class
# we can access the private attribute by using the name mangling technique
print(my_person._Person__gender) # this will work