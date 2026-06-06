#Happy Number


def sum_digits(n):
    sum=0
    while n>0:
        digit = n%10
        sum += digit**2
        n=n//10
    return sum
#
# def HappyNumber(n):
#     seen=set()
#     while True:
#         n = sum_digits(n)
#         if n in seen:
#             return False
#         seen.add(n)
#         if n==1:
#             return True
#
# n=int(input("Enter Number:"))
# print(HappyNumber(n))

def HappyNumber(n):
    slow = n
    fast = sum_digits(n)
    while fast!=1 and fast!=slow:
        slow = sum_digits(slow)
        fast = sum_digits(sum_digits(fast))

    return fast==1


n=int(input("Enter :"))
print(HappyNumber(n))





