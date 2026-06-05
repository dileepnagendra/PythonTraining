#Strings

# s = 'Hello'
# for i in s:
#     print(i)
#
# for i in range(len(s)):
#     print(s[i])

# s[0]="P"
# print(s)
#immutable
#ordered


# s="Hello"
# l=list(s)
# l[0]="P"
# # ['P', 'e', 'l', 'l', 'o']
# s = "".join(l)
# print(s) #Pello
#
# print("-".join(l)) #P-e-l-l-o
# print(" ".join(l)) #P e l l o
#
#
# s = "hello how are you"
# l= s.split()
# print(l) #['hello', 'how', 'are', 'you']
# print(s.split("o")) #['hell', ' h', 'w are y', 'u']
#
# s = "Hello"
# s = s.replace("l","L")
# print(s)
#
# s = "   helllo    "
# print(s)
# s=s.strip()
# print(s)
# s = "   helllo    "
# print(s.lstrip())
# print(s.rstrip())

#Remove white Spaces in a string
# s= "Hello How are you"
# # "HelloHowareyou"
#
# print("".join(s.split()))
# print(s.replace(" ",""))
# print(s.replace("o",""))

# l=s.split()
# s="".join(l)
# print(s)



# s="hello how r u"
# res = "" #or str()
#
# for i in s:
#     if i != " ":
#         res += i
# print(res)

# s = "hello"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)
# print(s[::-1])

#create an acronym
# s = input("Enter:")
# l=s.split()
# res = ""
# for i in l:
#     res += i[0]
# print(res)
#
# print("hello".upper()) #HELLO
# print("heLLo".lower()) #hello
# print("heLLo".islower()) #False
# print("HELLO".isupper()) #True
# print("HELLO".isalpha()) #True
# print("1324".isdigit())  #True
# print("abcd124".isalnum())

#Check a string is a palindrome or not

s = "Ma  l a--ya ,#lam."
#.mal#, ay--a l  aM
res = ""
for i in s.lower():
    if i.isalpha():
        res += i
print(res==res[::-1])
# if res==res[::-1]: print(True)
# else: print(False)

























