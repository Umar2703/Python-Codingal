import random
playing = True
number = random.randint(10,20)
print("I will generate a number from 10 to 20 and you have to guess the number one at a time")
print("the game when u get the correct guess")
while playing:
    guess= int(input("Give me ur best guess:"))
    if guess == number:
        print("U win the game")
        print("the number was:",number)
        break
    else:
        print("Ur guess isnt quiet right.Try again")