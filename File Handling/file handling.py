#File handling
import csv

#read - r
#write - w
#append - a
#create - x

# f = open("names.txt","w")
# f.write("Hello")
# f.close()
#
# with open("names.txt","w") as f:
#     f.write("hello")

# w  - overwrite a - append

#create mode
# with open("names2.txt","x") as f:
#     print(f)

#read mode
# with open("names.txt","r") as f:
#     s = f.read()
#     print(s)

#write mode
# with open("names.txt","w") as f:
#     f.write("Good Morning")

#append mode
# with open("names.txt","a") as f:
#     f.write("\nGood Night")
#
# with open("names.txt","r") as f:
#     print(f.read())
#
#     f.seek(0)
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#
#     f.seek(0)
#     print(f.readlines())


# with (open("names.txt","r") as f,
#       open("results.txt","a") as res):
#     for line in f.readlines():
#         marks = line.strip().split()
#         sum = 0
#         for i in range(1,len(marks)):
#             sum += int(marks[i])
#         res.write(f"{marks[0]} {sum}\n")

# temperatures = ["24 23 35 28 35\n",
#                 "25 28 22 21 26\n",
#                 "31 34 36 41 42"]
# with open("temperatures.txt","w") as f:
#     f.writelines(temperatures)

# with (open("temperatures.txt","r") as t,
#       open("avg.txt","a") as a):
#     for line in t.readlines():
#         temps = line.strip().split()
#         sum=0
#         for temp in temps:
#             sum += int(temp)
#         a.write(f"{sum/5}\n")
#
# import csv
students = [["Vikram","CSE"],["Rahul","ECE"]]
with open("students.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Dept"])
    writer.writerows(students)

#read as list
with open("students.csv","r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)

#read as Dictionary
with open("students.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)






























