#Sort Array By Frequency

nums = [2,3,1,3,2]
# nums.sort()
def freq(n):
    count=0
    for i in nums:
        if i==n:
            count+=1
    return count,-n

res = sorted(nums,key = freq)
print(res)
