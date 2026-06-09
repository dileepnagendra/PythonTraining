#Move Zeroes
l=[1,1,1,0,0,1,0]
# move all zeroes to the left
# output: [0,0,0,1,1,1,1]
#
# zeroes = []
# ones = []
# for i in l:
#     if i==0:
#         zeroes.append(i)
#     else:
#         ones.append(i)
# print(zeroes+ones)


l=[1,1,1,0,0,1,0]
#  0 1 2 3 4 5 6
left = 0
for right in range(len(l)):
    if l[right]==0:
        l[left],l[right] = l[right],l[left]
        left+=1
print(l)




