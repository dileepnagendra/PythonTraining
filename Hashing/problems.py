#Frequency of each number in a list

# l = [4,4,3,1,3,1,2,4,3,3,1,4]
# d={} #or dict()
# for i in l:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i]+=1
# print(d)
#
# d={}
# for i in l:
#     d[i] = d.get(i,0)+1
# print(d)


#387 First Unique character in a String


# def firstuniquechar(s):
#     d={}
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     for i in d:
#         if d[i]==1:
#             return s.index(i)
#     return -1
# s= "ababcadbedda"
# print(firstuniquechar(s))

#242 Valid Anagram

# #frequency of chars should be same in s and t
# def validAnagram(s,t):
#     d1={}
#     for i in s:
#         if i not in d1:
#             d1[i]=1
#         else:
#             d1[i]+=1
#     d2 = {}
#     for i in t:
#         if i not in d2:
#             d2[i] = 1
#         else:
#             d2[i] += 1
#     return d1==d2
# s="anagram"
# t="nagaram"
# print(validAnagram(s,t))



# def validAnagram(s,t):
#     from collections import Counter
#     return Counter(s)==Counter(t)
#
# s="anagram"
# t="nagaram"
# print(validAnagram(s,t))

#a string is Panagram
#
# def panagram(s):
#     res=""
#     for i in s.lower():
#         if i.isalpha():
#             res+=i
#     return len(set(res))==26
# s= "a quick, brown fox, jumps over .the Lazy dog!."
# print(panagram(s))

#1 Two Sum
# find two numbers which add upto target

l=[2,7,11,15,8]
target = 23
#
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print(i,j)
#             break


def twosum(nums,target):
    d={}
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in d:
            return d[complement],i
        else:
            d[nums[i]]=i
print(twosum([2,7,11,15],26))












