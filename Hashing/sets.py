#Hashing
# s= {5,6,7,7,7}
# print(s) #{5, 6, 7}
#mutable
#unordered
# s={"apple","banana","mango"}
# print(s)
# s={9,5,1,3,2}
# for i in s:
#     print(i)

# l=[9,3,1,4,6,6,3,4,2,3,2,4]
# #remove duplicates from the list.
# print(list(set(l)))
#
# #maintain the order. [9,3,1,4,6,2]
# l=[9,3,1,4,6,6,3,4,2,3,2,4]
# res=[]
# seen = set()
# for i in l:
#     if i not in seen:
#         res.append(i)
#         seen.add(i)
# print(res)

#217 Contains duplicate
# nums = [5,3,4,2,3,6]
#
# def Containsduplicate(nums):
#     seen = set()
#     for i in nums:
#         if i in seen:
#             return True
#         seen.add(i)
#     return False
# print(Containsduplicate(nums))
# #
# #
#
nums = [5,3,4,2,3,6]
#
# def Containsduplicate(nums):
#     seen = set()
#     for i in range(len(nums)):
#         if nums[i] in seen:
#             return i
#         seen.add(nums[i])
#     return -1
# print(Containsduplicate(nums))

#
# s=set()
# s.add(5)
# s.add(7)
# s.add(9)
# print(s)
# s.remove(9)
# print(s)
# # s.pop()
# print(s)

#Set operations
# s1= {"apple", "mango", "pineapple", "banana"}
# s2={"citrus","apple","orange","mango"}
#
# print(s1.union(s2))
# print(s1|s2)
# # {'orange', 'pineapple', 'mango', 'banana', 'apple', 'citrus'}
# print(s1.intersection(s2))
# print(s1&s2)
# print(s1.difference(s2))
# print(s1-s2)
# #{'pineapple', 'banana'}
# print(s2.difference(s1))
# print(s2-s1)
# # {'orange', 'citrus'}
# print(s1.symmetric_difference(s2))
# print(s1^s2)
# # {'orange', 'pineapple', 'banana', 'citrus'}
# s={1,2,3}
# s.discard(3)


def intersectionofarrays(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    s=s1&s2
    return list(s)
    # return list(set(nums1)&set(nums2))
nums1 = [9,4,2,5]
nums2 = [8,9,5,3]
print(intersectionofarrays(nums1,nums2))
