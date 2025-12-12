print("select ur ride:")
print("1.Bike")
print("2.Car")
choice=int(input("enter ur choice"))
if choice==1:
    print("WHat type of bike")
    print("1.Scooty")
    print("2.Scooter")
    choice2= int(input("Enter your choice"))
    if choice2==1:
        print("u have selected scooty")
    else:
        print("u have selected scooter")
elif choice == 2:
    print("what type of car ")
    print("1.Sedan")
    print("2.SuV")
    choice3 = int(input("Enter your choice"))
    if choice3 ==1:
       print("u have slected Sedan") 
    else:
        print("U have selected Suv")
else:
    print("Wrong Choice")        