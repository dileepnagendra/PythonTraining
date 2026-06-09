#Valid Parenthesis

# [{]})] -> not valid
# [{}] ->valid

s= "[({)}]"
def validparenthesis(s):
    stack = []
    for i in s:
        if i=="(": stack.append(")")
        elif i=="[" : stack.append("]")
        elif i=="{" : stack.append("}")
        else:
            if not stack or i != stack.pop():
                return False
    return True if not stack else False
print(validparenthesis(s))




