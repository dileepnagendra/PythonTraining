# factors of a number
#
n = int(input("Enter number:"))
sum=0
for i in range(1,n+1):
    if n % i ==0:
        print(i)
        sum += i
print("Sum of factors:",sum)

n = int(input("Enter number:"))
sum=0
for i in range(1,n//2+1):
    if n % i ==0:
        sum += i
if sum==n : print("Perfect Number")
elif sum>n : print("Abundant Number")
else: print("Deficient Number")






