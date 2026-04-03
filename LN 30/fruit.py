import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange','watermelon':'green','banana':'yellow'}
def quiz(self):
    while (True):
        fruit, color=random.choice(list(self,fruit.item()))
        print("What is the color of" ,fruit)
        user_answer=input()
        if(user_answer.lower()==color):
            print("Correct answer")
        else:
            print("wrong answer")
        option=int(input("enter 0,if u want to play again otherwise enter 1:  "))