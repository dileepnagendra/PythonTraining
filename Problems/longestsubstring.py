#length of longest substring with same charcters

s = "aacaabbbcabbbbb" #3

count=1
maxcount=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
        maxcount = max(maxcount, count)
    else:
        count=1
print(maxcount)





