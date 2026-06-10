#Two Sum II

def twosumII(l,target):
    i = 0
    j = len(l)-1
    while i<j:
        sum = l[i] + l[j]
        if sum==target:
            return [i+1,j+1]
        elif sum > target:
            j-=1
        else:
            i+=1
l=[2,5,7,11,13]
target = 18
print(twosumII(l,target))




