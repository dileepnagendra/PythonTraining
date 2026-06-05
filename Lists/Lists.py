l = [1,2,3,4,5,6]

# fixed  - dynamic
#homogenous - heterogenous
#mutable
#ordered

# l = [1,2,3,4,5,6]
# #    0 1 2 3 4 5
# #   -6-5-4-3-2-1
#
# l[4] = 50
# l[-2]=5
# print(l)
#
# l = [7,3,9,12,6,2]
# #    0 1 2 3 4 5
# #   -6-5-4-3-2-1
# #
# for i in range(len(l)):
#     print(l[i])
#
# for i in l:
#     print(i)

# l = [7,3,9,12,6,2]
# #find the sum of all even numbers in the list
# sum=0
# for i in l:
#     if i%2==0:
#         sum += i
# print(sum)

#find the sum of all even indexed numbers
# in the list

# l = [7,3,9,12,6,2]
# sum = 0
# for i in range(len(l)):
#     if i%2==0:
#         sum += l[i]
# print(sum)

#List Methods

# l = []
# # l = list()
# l.append(5)
# l.append(8)
# l.append(2)
# print(l)
# l.insert(0,10)
# print(l)
# l.insert(6,12)
# print(l) #[10, 5, 8, 2, 12]
# l.extend([35,36])
# # l.append([35,36])
# # l.extend("hello")
# # l.append("hello")
# print(l)
# l2 = ["a","b","c"]
# print(l+l2)

l=["apple","mango","banana","pineapple"]
# l.remove("banana")
# print(l)
# l.pop(1)
x = l.pop()
print(x)
print(l)
# l.clear()
# print(l)
# del l[2]
# print(l)
# del l
# print(l)

#
# create a list of numbers divisble by 3 & 7
# but not by 2 from 1 to 100

l =[]
for i in range(1,101):
    if (i%3==0 and i%7==0) and i%2!=0:
        l.append(i)
print(l)

#remove all odd numbers from the list.
# l=[1,3,5,7,9]
# for i in l.copy():
#     if i%2 !=0:
#         l.remove(i)
# print(l)


















