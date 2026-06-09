#rotate the array towards right two times
# output : [1,7,6,3,8,5]
# l=[6,3,8,5,1,7]
# #  0 1 2 3 4 5
# k = 9
# n=len(l)
# k=k%n
# print(l[n-k:] + l[:n-k])


l=[6,3,8,5,1,7]
k=4
def rev(left,right):
    while left<right:
        l[left],l[right] = l[right],l[left]
        left+=1
        right-=1
n=len(l)
k=k%n
rev(0,n-1)
rev(0,k-1)
rev(k,n-1)
print(l)





