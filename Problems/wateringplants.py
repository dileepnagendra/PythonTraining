#Watering Plants

plants = [2,3,2,4]
k=5
def wateringplants(plants,k):
    capacity = k
    steps=0
    for i in range(len(plants)):
        if capacity>=plants[i]:
            capacity -= plants[i]
            steps+=1
        else:
            steps += 2*i + 1
            capacity = k
            capacity -= plants[i]
    return steps
print(wateringplants(plants,k))
