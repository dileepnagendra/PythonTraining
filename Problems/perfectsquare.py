#Check a number is a perfect square or not
#
# def isperfect(n):
#     for i in range(1,n+1):
#         if i*i==n:
#             return True
#     return False
# print(isperfect(19))
#
# import math
# def isperfect(n):
#     return int(math.sqrt(n)) == math.sqrt(n)
# print(isperfect(16))




def isperfect(n):
    left = 0
    right = n
    while left<=right:
        mid = (left+right)//2
        if mid*mid==n:
            return True
        elif n>mid*mid:
            left = mid+1
        else:
            right = mid-1
    return False
print(isperfect(16))








