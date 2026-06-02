#Prime Number

# n=int(input("Enter a Number;"))
# isPrime = True
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#         isPrime = False
#         break
# if isPrime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")
#
#
# n=28
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#         print("Not a Prime Number")
#         break
# else:
#     print("Prime Number")


def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(IsPrime(7))
print(IsPrime(17))
print(IsPrime(18))