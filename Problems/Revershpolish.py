#Evaluate reversh polish notation

l = ["2","3","5","*","+"]
def Evaluatepostfix(l):
    stack = []
    for i in l:
        if i.isdigit():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == "+":stack.append(a+b)
            elif i=="-":stack.append(a-b)
            elif i == "*": stack.append(a * b)
            elif i=="/":stack.append(int(a/b))
    return stack[0]
print(Evaluatepostfix(l))



