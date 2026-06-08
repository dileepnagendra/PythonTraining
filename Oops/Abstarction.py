#Abstraction
# Showing neccesary info
# hiding unneccesary things

#abstraction is abput hiding internal implementation

from abc import ABC, abstractmethod
class Shape(ABC): #abstract class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def dimensions(self):
        return self.area(),self.perimeter()

class Circle(Shape):
    def area(self,r):
        return 3.14*r*r
    def perimeter(self,r):
        return 2*3.14*r
c=Circle()
print(c.area(5))
print(c.perimeter(5))


class Customer(ABC):
    def __init__(self,name,acno,balance):
        self.name = name
        self.acno = acno
        self.balance = balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def checkbalance(self):
        print("Balance:",self.balance)










