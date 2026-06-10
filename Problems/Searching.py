#Linear search
# l = [2,5,8,11,16,19,23,29,34,43]
# target = 23
# for i in l:
#      if i==target:
#          print("Found")
#          break
# else:print("Not found")

#Binary Search
l = [2,5,8,11,16,19,23,29,34,43]
def binarysearch(l,target):
    left = 0
    right = len(l)-1
    while left<=right:
        mid = (left+right)//2
        if l[mid]==target:
            return True
        elif target>l[mid]:
            left = mid+1
        else:
            right = mid-1
    return False
print(binarysearch(l,29))

