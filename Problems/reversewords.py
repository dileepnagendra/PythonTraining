
s = "this is the question"
l=s.split()
print(l)
# ['this', 'is', 'the', 'question']
rev = l[::-1]
# ['question', 'the', 'is', 'this']
s= " ".join(rev)
print(s) #question the is this
print(s[::-1]) #siht si eht noitseuq

s = "this is the question"
print(" ".join(s.split()[::-1]))

