from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age 

    @abstractmethod
    def role(self):
        pass


#Person1 = Person("Milo", 19)
#print(Person1.name)
#print(Person1.get_age())
# using get_age() is better because it avoids accidental modification 

class student(Person):
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age

    def role(self):
        return f"{self.name} is a student"

student1 = student("Bearbrand", 16)
print(student1.name, "is studying")
print(student1.get_age())
print(student1.role())

class teacher(Person):
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age

    def role(self):
        return f"{self.name} is a teacher"

teacher1 = teacher("Energen", 31)
print(teacher1.name, "is teaching")
print(teacher1.get_age())
print(teacher1.role())

