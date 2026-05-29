# for i in range(10):
#     print("hello")

# # for _ in range(10):
# #     print("hello")

# for i in range(1,101):
#     if i%5==0:
#         print(i)

# for i in range(1,101,2):
#     print(i)

# for i in range(1,101):
#     if i%2 !=0:
#         print(i)

# for i in range(10,0,-1):
#     print(i)

# sum=0
# for i in range(1,101):
#     if i%7==0:
#         sum = sum +i
# print(sum)

# #Print multiplication table of any number upto 10.
# n = int(input("Enter Number : "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


n = 12
count=0
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    count+=1
print(count)
