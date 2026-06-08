#Polymorphism -> many forms

class Sum:
    def add(self,a,b,c=0):
        if c==0:
            return a+b
        else:
            return a*b*c

s=Sum()
print(s.add(4,5,6))

#Encapuslation
#wrapping of things into a single component

#access keyboards -> private,public,protected
class Customer:
    def __init__(self,name,acno,balance):
        self.name = name
        self.acno = acno
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def checkbalance(self):
        print("Balance:",self.__balance)
c = Customer("Vikram",123,10000)
c.checkbalance()
c.deposit(500)

