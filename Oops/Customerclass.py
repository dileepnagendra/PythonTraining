class Customer:
    def __init__(self,name,acno,balance):
        self.name = name
        self.acno = acno
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited Succesfully")
        self.checkbalance()
    def withdraw(self):
        if amount > self.balance:
            print("Insufficient funds")
            self.checkbalance()
        else:
            self.balance += amount
            print("Withdrawn Succesfully")
            self.checkbalance()
    def checkbalance(self):
        print("Balance:",self.balance)
c1 = Customer("Vikram",123,10000)
c2 = Customer("Rahul",456,5000)
c1.checkbalance()
c1.deposit(5000)


