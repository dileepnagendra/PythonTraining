# def sumofsquares(a,b):
#     c = a*a + b*b
#     return c
# x = sumofsquares(4,5)
# print(x)

# def sumofsquares(a,b):
#     c = a*a + b*b
#     print(c)
# x = sumofsquares(4,5)
# print(x)


# "Vikram" -> "Good Morning Vikram"

def greet(name):
    return f"Good Morning {name}"

print(greet("Vikram"))
print(greet("Karthik"))

#Create a fuction temprature convertor f to c.

# def tempConv(f):
#     c = (f-32)*(5/9)
#     return c
# f = float(input("Enter Temperature in F:"))
# c = tempConv(f)
# print(f"temperature in C: {c:.2f}")




# def currconv(amount,cur):
#     if cur == "usd" or cur =="eur":
#         return amount * 0.01
#     elif cur == "aed":
#         return amount * 0.04
#     elif cur == "yen":
#         return amount * 2
 

# amount = int(input("Enter amount:"))
# cur = input("Enter cur (usd,eur,yen,aed):")
# res = currconv(amount,cur)
# print(res,cur)


# def calc(a,b):
#     return a+b,a-b,a*b
# add,sub,pro = calc(4,5)
# print(add)
# print(sub)
# print(pro)


def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(IsPrime(7))
print(IsPrime(17))
print(IsPrime(18))























