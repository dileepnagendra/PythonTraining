# Nested Loops

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

#find all prime numbers from 1 to 100



for n in range(2,101):
    isPrime = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            isPrime = False
            break
    if isPrime:
        print(n)




