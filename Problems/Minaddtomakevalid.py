#Min add to make it valid

s="))()(("
open,closed = 0,0
for i in s:
    if i == "(":
        open+=1
    else:
        if open > 0: open -=1
        else: closed +=1
print(open+closed)