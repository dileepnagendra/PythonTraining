# from collections import Counter
# s="tree"
# d= Counter(s) #{'e': 2, 't': 1, 'r': 1}
# def freq(c):
#     return d[c]
# res = sorted(s,key = freq,reverse=True)
# print("".join(res))

from collections import Counter
s="tree"
d= Counter(s) #{'e': 2, 't': 1, 'r': 1}
res = sorted(s,key = lambda c:d[c],reverse=True)
print("".join(res))
