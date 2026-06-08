
# a=6
# b=12
# count=0
# for i in range(1,min(a,b)+1):
#     if a % i ==0 and b%i==0:
#         hcf = i
#         count+=1
# print(count)
# print("GCD:",hcf)
# # a x b = gcd x lcm
# print("LCM:",(a*b)//hcf)

#Euclids theorem
#continue replacing a with b
# b with a%b until b equals zero.
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(24,36))



