#Exception Handling

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     print(a/b)
# except ValueError:
#     print("give valid integer only")
# except ZeroDivisionError:
#     print("Cant divibe by zero")
# else:
#     print(a+b)
#     print(a*b)
#     print(a-b)
#
# #Exception Handling
#
#
# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
# except ValueError:
#     print("give valid integer only")
# else:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("cant divide by zero/")
#     print(a+b)
#     print(a*b)
#     print(a-b)


#
# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     print(a/b)
# except ValueError:
#     print("give integers only")
# except ZeroDivisionError:
#     print("cant divide by zero")
# else:
#     print(a+b)


l=[6,8,3,4]
try:
    i = int(input("Enter index:"))
    print(l[i])
except ValueError:
    print("give integers only")
except IndexError:
    print("give index less than",len(l))
except Exception as e:
    print(e)



# marks=["3","6","ab","7","ab"]
# sum=0
# for i in marks:
#     try:
#         sum += int(i)
#     except ValueError:
#         continue
# print(sum)


#Raise an exception

class LowBalanceException(Exception):
    pass

balance = 10000
amount = int(input("Enter amount to withdraw:"))
try:
    if amount>10000:
        raise LowBalanceException("insuffcient funds")
except LowBalanceException as e:
    print(e)
else:
    balance -= amount
    print("Withdraw succesful")
finally:
    print("Visit again")









