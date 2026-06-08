

c = [[5,2], [5,4], [10,3], [20,1]]
chef_free  = 0
total=0
for i in c:
    if i[0] >= chef_free:
        chef_free = i[0] + i[1]
        waiting_time = chef_free - i[0]
    else:
        chef_free = chef_free + i[1]
        waiting_time = chef_free - i[0]
    total += waiting_time

print(total/len(c))






