import random
while True :
    user  = input("Enter a choice (rock,paper,scissors):")
    options = ["rock","paper","scissors"]
    computer= random.choice(options)
    print("U chose",user)
    print("computer chose",computer)
    if user==computer:
        print("Both players selected,",user,"Its a tie")
    elif user=="rock":
        if computer=="scissors":
            print("Rock smashes scissors! you win!")
        else:
            print("Paper covers rock ! U lose")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! u win!")
        else:
            print("Rock smashes scissors! U lose!")
    play_again = input("PLay again?(y/n);")            
    if play_again != "y":
        break