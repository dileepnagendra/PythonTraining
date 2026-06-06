#Maximum subarray sum
# # find the maximum subarray sum
# l=[2,-3,4,6,2,8,-9,7]
# max=l[0]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         s = sum(l[i:j+1])
#         if s>max:
#             max =s
# print(max)

def maxsubarraysum(l):
    cur_sum=0
    max_sum=l[0]
    for i in l:
        cur_sum+=i
        max_sum=max(max_sum,cur_sum)
        if cur_sum<0:cur_sum=0
    return max_sum
l=[2,4,-3,-4,8,2,-2,4,-5]
print(maxsubarraysum(l))



