s="3-598-21507-X"
s = s.replace("-","")
print(s)
sum=0
z=10
for i in s:
    if i=="X":
        i="10"
    sum = sum + int(i)*z
    z=z-1
if sum%11==0:print("valid ISBN")
else:print("Invalid ISBN")



