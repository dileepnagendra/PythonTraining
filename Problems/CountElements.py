#Count Elements

def countelements(l):
    a = min(l)
    b = max(l)
    count=0
    for i in l:
        if a<i<b:
            count+=1
    return count
print(countelements([3,9,2,6]))
