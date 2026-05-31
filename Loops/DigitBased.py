#Sum of Digits
# n=46591
# sum=0
# while n>0:
#     digit = n%10
#     sum += digit
#     n=n//10
# print("Sum of Digits :",sum)


# Find the absolute difference between even digits
# and odd digits in a given number.

# print(abs(7-3)) #4
# print(abs(3-7)) #4
#
# n=int(input("Enter a number:"))
# sum1,sum2=0,0
# while n>0:
#     digit = n%10
#     if digit%2==0:
#         sum1 += digit
#     else:
#         sum2 += digit
#     n=n//10
# print("Absolute difference:",abs(sum1-sum2))


# Reverse a Number
#
# n = 1221
# temp = n
# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev*10 + digit
#     n=n//10
# print("Reversed Number :",rev)
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


#Armstrong number -
# Sum of digits where each digit raised to the number of
# digits should be equal to the same number
#153 -> 1^3 + 5^3 + 3^3 = 153

n = int(input("Enter number :"))
count=0
x,y=n,n
while x>0:
    x=x//10
    count+=1
sum=0
while y>0:
    digit = y%10
    sum = sum+digit**count
    y=y//10
if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")








