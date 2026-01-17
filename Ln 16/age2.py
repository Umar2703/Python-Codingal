try:
    age=int(input("Enter age:"))
    if age<18:
        raise ValueError
    else:
        print("age is valid")

except ValueError:
    print("age is invalid")        