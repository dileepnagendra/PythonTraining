#Exception Handling


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)
except ValueError:
    print("give valid integer only")
except ZeroDivisionError:
    print("Cant divibe by zero")
else:
    print(a+b)
    print(a*b)
    print(a-b)

#Exception Handling


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
except ValueError:
    print("give valid integer only")
else:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("cant divide by zero/")
    print(a+b)
    print(a*b)
    print(a-b)

