medical_cause= input("did u have a medical cause Y or N  ")
attendance = int(input("enter the attendance:"))
if medical_cause== "Y":
    print("you are allowed")
else:
    if attendance>=75:
        print("u r alllowed")
    else:
        print("u r not allowwed")    