# age = int(input("Enter age:"))
# if age>18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# day = int(input("Enter number:"))
# if day==0:
#     print("Sunday")
# elif day==1:
#     print("Monday")
# elif day==2:
#     print("Tuesday")
# else:
#     print("Holiday")

# username = "dileep"
# password = "dileep123"

# user = input("Enter username: ")
# if user == username:
#     psw = input("Enter password: ")
#     if psw == password:
#         print("Succesful login")
#     else:
#         print("Incorrect password")
# else:
#     print("incorrect username")


salary = int(input("Enter salary:"))
if salary <=50000:
    exp = int(input("Enter experience:"))
    if exp>=3:
        salary = salary + salary*0.3
    else:
        salary = salary + salary*0.2
else:
    salary = salary + salary*0.1
print("Updated Salary: ",salary)





















