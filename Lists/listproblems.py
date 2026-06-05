# #maximum number in list
# l = [9,2,13,8,7,14,6,5]
# max = l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)
#
# min = l[0]
# for i in l:
#     if i<min:
#         min=i
# print(min)


# l = [9,3,13,10,5]
# max1 = l[0]
# max2 = 0
# for i in l:
#     if i>max1:
#         max2 = max1
#         max1 = i
#     elif i>max2 and i<max1:
#         max2=i
# print(max1)
# print(max2)
#
# print(min(l),max(l),sum(l),sum(l)/len(l),l.count(3))

#create a func to find the frequenCY OF A  number in list

# l=[5,4,3,1,2,3,3,7,3,3,1,2]
# # print(l.count(3))
# def freq(l,target):
#     count=0
#     for i in l:
#         if i==target:
#             count+=1
#     return count
# print(freq(l,3))

# print(sorted(l1+l2))
a = [2,3,5,9]
b = [8,12,19,24]
def mergetwolists(a,b):
    i=0
    j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    if i==len(a):res.extend(b[j:])
    elif j==len(b):res.extend(a[i:])
    return res
print(mergetwolists(a,b))











