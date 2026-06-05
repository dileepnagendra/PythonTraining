#Dictionary (HashMap)

# s="1234431443"
#
# d={
#     "1":2,
#     "2":1,
#     "3":3,
#     "4":4
# }
#
# #d[key]=value
# print(d["3"])

# d={
#     "name":"Vikram",
#     "rno" : 1234,
#     "cgpa" : 9.5,
#     "hobbies" : ["reading","sleeping"]
# }
# print(d)
# d["cgpa"] = 9.2 #if key exists, it updates
# d["age"] = 21 #if key doesnt exists, it inserts
# print(d)
# d["age"] += 1
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())

d={'name': 'Vikram', 'rno': 1234,
   'cgpa': 9.2,
   'hobbies': ['reading', 'sleeping'],
   'age': 22}

# for i in d:
#     print(i,d[i]) #i->key, d[i]->value
# print(d.pop("age"))
# print(d["marks"])
# print(d.get("marks",0))




# l=[9,3,4,6]
# for i,val in enumerate(l):
#     print(i,val)
#
# for i in range(len(l)):
#     print(i,l[i])

