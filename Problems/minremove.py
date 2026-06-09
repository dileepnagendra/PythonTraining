#Min remove to make it valid
s="n)i)t(t)(e("  #-> "nit(t)e"
stack = []
open=0
for i in range(len(s)):
    if s[i] == "(":
        open+=1
        stack.append(i)
    elif s[i] == ")":
        if open > 0:
            open -=1 
            stack.pop()
        else:
            stack.append(i)
res= ""
for i in range(len(s)):
    if i not in stack:
        res += s[i]
print(res)

