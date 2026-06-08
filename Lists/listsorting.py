#List sorting
#arranging elements in a specific order
# l=[9,12,3,-5,8,11,2,0,-7]
# l.sort()
# print(l) #[-7, -5, 0, 2, 3, 8, 9, 11, 12]
# l.sort(reverse = True)
# print(l) #[12, 11, 9, 8, 3, 2, 0, -5, -7]
# s = sorted(l)
# print(s) #[-7, -5, 0, 2, 3, 8, 9, 11, 12]
# s = sorted(l,reverse = True)
# print(s) #[12, 11, 9, 8, 3, 2, 0, -5, -7]
# print(l) #[9, 12, 3, -5, 8, 11, 2, 0, -7]


l=["Faisel","Adeeb","Ann Sandra","Ananya","Bryan","Dileep"]
# l.sort()
# print(l)
#['Adeeb', 'Ananya', 'Ann Sandra', 'Bryan', 'Dileep', 'Faisel']

#Sort the above list based on the length of strings
l.sort(key = len)
print(l)
# ['Adeeb', 'Bryan', 'Ananya', 'Dileep', 'Faisel', 'Ann Sandra']
l.sort(key = len,reverse = True)
print(l)
# ['Ann Sandra', 'Faisel', 'Ananya', 'Dileep', 'Adeeb', 'Bryan']


l=["Faisel","Adeeeb","Ann Sandraaa","Ananya","Bryan","Dilip"]
#sort the above names based on the number of vowels
def vowelscount(s):
    count =0
    for i in s:
        if i in "aeiouAEIOU":
            count+=1
    return count

l.sort(key = vowelscount)
print(l)
# ['Bryan', 'Dilip', 'Faisel', 'Ananya', 'Adeeeb', 'Ann Sandraaa']










