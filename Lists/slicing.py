#List Slicing

#creating a copy of a portion from the list
#
# l[start:end:step]

l=[6,9,5,4,7,8,3]
#  0 1 2 3 4 5 6
#
print(l[2:5])  #[5, 4, 7]
print(l[2:6:2]) #[5, 7]
print(l[3:]) #[4, 7, 8, 3]
print(l[:3]) #[6, 9, 5]
print(l[1:10:3]) #[9,7]
print(l[::2]) #[6, 5, 7, 3]
print(l[2:6:-2]) #[]
print(l[2:2]) #[]
print(l[5:1:-1]) #[8,7,4,5]


l=[6,9,5,4,7,8,3]
#  0 1 2 3 4 5 6
# -7-6-5-4-3-2-1
print(l[-6:-2]) #[9, 5, 4, 7]
print(l[-2:-6]) #[9, 5, 4, 7]
print(l[-3:]) #[7,8,3]
print(l[2:-2]) #[5, 4, 7]
print(l[:]) #[6, 9, 5, 4, 7, 8, 3] #copy
print(l[::-1]) #[3, 8, 7, 4, 5, 9, 6] #reverse


