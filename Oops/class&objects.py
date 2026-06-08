#oops - Object oriented programming
#
# class - a blueprint for an object
# object - an instance of a class

class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    def __repr__(self):
        return f"Name :{self.name}, Age:{self.age}"
    def sound(self):
        return "Boooooow-Bow"
d1 = Dog("Simba",3,"Husky") #Constructor
d2 = Dog("Tommy",10,"lab")
# print(d1.breed)
# print(d1.sound())
# print(d2.age)
print(d1)
print(d2)

