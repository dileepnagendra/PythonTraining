s = '''The campus is the only private 
    campus in the city The atmosphere is so
    good that it becomes the best campus i have
    visited in the recent times.'''
def wordfrequency(s):
    words = s.lower().split()
    d={}
    from collections import Counter
    d= Counter(words)
    max=0
    for i in d:
        if d[i]>max:
            max=d[i]
            res = i
    return res
print(wordfrequency(s))






