#Nested Lists
# l=[[4,5,6],[6,7],[5,9,3,2]]

# print(l[0])
# s=[4,5,6]
# print(l[0][0])
# print(l[2][1])
# l=[[4,5,6],[6,7],[5,9,3,2]]

# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j])

# l=[["vikram",45,56,78,64,30],["karthik",55,76,88,44,60],
# ["rahul",85,86,78,54,80],["viswa",95,66,58,74,90]]

# res=[]
# for i in range(len(l)):
#     sum=0
#     n=len(l[i])
#     s=[]
#     for j in range(1,n):
#         sum += l[i][j]
#     s.extend([l[i][0],sum,sum/(n-1)])
#     res.append(s)
# print(res)

# l=[["vikram",45,56,78,64,30],["karthik",55,76,88,44,60],
# ["rahul",85,86,78,54,80],["viswa",95,66,58,74,90]]

# res=[]
# for i in range(len(l)):
#     res.append((l[i][0]))
# print(res)
#
# ans=[]
# for i in l:
#     ans.append(i[0])
# print(res)
#
# l=[[4,5,9,3],
#    [6,8,7,2],
#    [1,9,3,7],
#    [8,2,6,4]]

# for row in range(len(l)):
#     for col in range(len(l[0])):
#         print(l[row][col])

#
# l=[[4,5,9,3],
#    [6,8,7,2],
#    [1,9,3,7],
#    [8,2,6,4]]

# sum=0
# for i in range(len(l)):
#         sum += l[i][i]
# print("Right diagnol sum:",sum)
#
# sum=0
# n=len(l)
# for i in range(len(l)):
#         sum += l[i][n-i-1]
# print("Left diagnol sum:",sum)

# l=[[4,5,9,3],
#    [6,8,7,2],
#    [1,9,3,7],
#    [8,2,6,4]]
# t = []
# for i in range(len(l[0])):
#     t.append([0]*len(l))
# for i in range(len(l)):
#     for j in range(len(l[0])):
#         t[j][i] = l[i][j]
# print(t)

l=[[4,6,1,8],
   [5,8,9,2],
   [9,7,3,6],
   [3,2,7,4]]

for i in range(len(l)):
    for j in range(i+1,len(l[0])):
        l[i][j],l[j][i] = l[j][i],l[i][j]
print(l)






















