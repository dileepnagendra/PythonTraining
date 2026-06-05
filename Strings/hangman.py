print("Welcome to tha game")
import random

words = ["animal","college","umbrella","syntax","intermediate",
         "landrover","aeroplane"]
selected = "animal"
word = list(selected)
guessed = [ "_" for i in range(len(word))]
print(" ".join(guessed))
while True:
    guess = input("Enter guess:").lower()
    if guess in word:
        index = word.index(guess)
        guessed[index]=guess
        word[index] = "#"
    else:
        print("Wrong guess")
    s = " ".join(guessed)
    print(s)
    if(s.replace(" ","")==selected): break;




