#Inheritance
# class Father:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     haircolor = "Black"
#     def work(self):
#         return "I will work 10hrs a day"
# class Son(Father):
#     def __init__(self,fname,lname,nickname):
#         # self.fname=fname
#         # self.lname=lname
#         super().__init__(fname,lname)
#         self.nickname = nickname
#     haircolor = "Blue"
#     def work(self):
#         # print(super().work())
#         return "I dont want to work"
# f = Father("Junaid","Ahmed")
# s= Son("zaid","Ahmed","zid")
# print(s.work())

#method overiding : when a child class overrides
# the method inherited form its parent class

#Multiple Inheritance:
# a child class inheriting multiple parent classes

# class Father: #Method Resolution order
#     haircolor = "Black"
# class Mother:
#     haircolor = "Brown"
# class Son(Father,Mother):
#     pass
# s=Son()
# print(s.haircolor) #black


#Multilevel inheritance
class A:
    color = "blue"
class B(A):
    pass
class C(B):
    pass
c=C()
print(c.color) #blue


# create a bike (parent class) and a func sound()
#create a child class ktm and modify the sound()

class Bike:
    def sound(self):
        return "Zuuuuiiii"
class RE(Bike):
    def sound(self):
        return "DuDUDUDUDu"
r=RE()
print(r.sound())






