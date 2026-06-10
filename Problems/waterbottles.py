#Water Bottles


def waterbottles(numBottles,numExchange):
    drunk = numBottles
    empty = numBottles
    while empty >= numExchange:
        new = empty//numExchange
        drunk += new
        empty = empty%numExchange + new
    return drunk

numBottles = 15
numExchange = 4
print(waterbottles(numBottles,numExchange))
