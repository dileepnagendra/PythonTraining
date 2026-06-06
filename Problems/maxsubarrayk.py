#Max sum subarray of size K.
l=[7,12,3,7,10,2,1,18,5]
#  0 1  2 3  4 5 6  7 8
k=5
def maxsumsubarrayk(l,k):
    sum = 0
    for i in range(k):
        sum += l[i]
    max_sum = sum
    for i in range(k,len(l)):
        sum = sum + l[i] - l[i-k]
        if sum>max_sum: max_sum=sum
    return max_sum
print(maxsumsubarrayk(l,k))




